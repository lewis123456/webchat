from django.django_model import db


class User(db.Model):
	id = db.PositiveBigAutoField(primary_key=True)
	user_name = db.CharField(max_length=128)
	salt = db.CharField(max_length=64)
	pwd_md5 = db.CharField(max_length=128)
	create_time = db.PositiveIntegerField()
	update_time = db.PositiveIntegerField()

	class Config:
		db_for_write = 'webchat_db.write'
		db_for_read = 'webchat_db.read'

	class Meta:
		db_table = u'user_tab'
