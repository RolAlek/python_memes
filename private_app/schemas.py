from pydantic import BaseModel, Field, field_validator


class CreateMeme(BaseModel):
    name: str = Field(..., min_length=1, max_length=64)

    @field_validator('name')
    @classmethod
    def name_cant_be_null(cls, value):
        if value is None:
            raise ValueError('Мемы должны радовать, а не null!')
        return value


class UpdateMeme(CreateMeme):
    name: str | None = Field(None, min_length=1, max_length=64)
    url: str | None = Field(None)
    file_name: str | None = Field(None)
