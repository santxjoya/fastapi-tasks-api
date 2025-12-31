from sqlalchemy.orm import Session
from typing import List

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


def create_task(
    db: Session,
    *,
    user_id: int,
    task_in: TaskCreate
) -> Task:
    task = Task(
        title=task_in.title,
        description=task_in.description,
        owner_id=user_id,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(
    db: Session,
    *,
    user_id: int,
    skip: int = 0,
    limit: int = 10
) -> List[Task]:
    return (
        db.query(Task)
        .filter(Task.owner_id == user_id)
        .order_by(Task.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_task_by_id(
    db: Session,
    *,
    task_id: int,
    user_id: int
) -> Task | None:
    return (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.owner_id == user_id
        )
        .first()
    )


def update_task(
    db: Session,
    *,
    task: Task,
    task_in: TaskUpdate
) -> Task:
    data = task_in.model_dump(exclude_unset=True)

    for field, value in data.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, *, task: Task) -> None:
    db.delete(task)
    db.commit()
