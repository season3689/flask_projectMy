from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length



class UserForm(FlaskForm):
    username = StringField(
        "닉네임",
        validators=[
            DataRequired(message='닉네임은 필수입니다.'),
            Length(max=30, message="30문자 이내로 입력해 주세요. "),
        ],
    )
    textword = StringField(
        "문제",
        validators=[
            DataRequired(message='문제는 필수입니다.'),
            Length(max=50, message="50문자 이내로 입력해 주세요. "),
        ]
    )
    answer = StringField(
        "정답",
        validators=[
            DataRequired(message='정답은 필수입니다.'),
            Length(max=20, message="20문자 이내로 입력해 주세요. "),
        ]
    )
    password = PasswordField(
        "비밀 번호",
        validators=[DataRequired(message="비밀번호는 필수입니다. ")]
    )
    submit = SubmitField("신규 등록")