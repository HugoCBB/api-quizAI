from sqlalchemy.orm import Session
from app.domain.user import UserInput
from app.infra.models.user_model import UserModel

class UserRepository:
    def save(self, db: Session, input: UserInput):
        output = UserModel(
            name=input.name,
            email=input.email,
            password=input.password
        )
        db.add(output)
        db.commit()
        db.refresh(output)
        return output
    
    def get_user_by_email(self, db: Session, email: str):
        return db.query(UserModel).filter(UserModel.email == email).first()