from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship

from src.database import Base


class Friend(Base):
    """Таблица друзей"""

    __tablename__ = 'friends_association'

    id = Column(
        Integer,
        primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey('users.id')
    ),
    friend_id = Column(
        Integer,
        ForeignKey('users.id')
    )


class User(Base):
    """Таблица пользователя"""

    __tablename__ = 'users'

    id = Column(
        Integer,
        primary_key=True
    )
    name = Column(
        String,
        nullable=False
    )
    email = Column(
        String,
        unique=True,
        nullable=False
    )
    hashed_password = Column(
        String,
        nullable=False
    )
    friends = relationship(
        'Friend',
        foreign_keys='Friend.user_id',
        backref='user'
    )
    friend_of = relationship(
        'Friend',
        foreign_keys='Friend.friend_id',
        backref='friend'
    )


class Message(Base):
    """Таблица сообщений"""

    __tablename__ = 'messages'

    id = Column(
        Integer,
        primary_key=True
    )
    sender_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False
    )
    receiver_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False
    )
    content = Column(
        Text,
        nullable=False
    )
    create_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
    is_read = Column(
        Boolean,
        default=False,
        nullable=False
    )

    sender = relationship(
        'User',
        foreign_keys=[sender_id],
        backref='sent_messages'
    )
    receiver = relationship(
        'User',
        foreign_keys=[receiver_id],
        backref='received_messages'
    )