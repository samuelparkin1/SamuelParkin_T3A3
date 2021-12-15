from main import db
from models.user import User

enrolments = db.Table(
    'enrolments',
    db.Column('user_id', db.Integer, db.ForeignKey('flasklogin-users.id'), primary_key=True),
    db.Column('trip_id', db.Integer, db.ForeignKey('trips.trip_id'), primary_key=True)
)

# Our first model! 
# This tells the ORM what tables should exist in the database
# It also lets us retrieve info from those tables
class Trip(db.Model):
    # The tablename attribute specifies what the name of the table should be
    __tablename__ = "trips"

    # These attributes specify what columns the table should have
    trip_id = db.Column(db.Integer, primary_key=True)
    pick_up = db.Column(db.String(80), nullable=False)
    destination = db.Column(db.String(200), nullable=False)
    cost = db.Column(db.Integer, nullable=False, server_default="0")

    user_profile = db.Column(db.Integer, db.ForeignKey('flasklogin-users.id'))

    students = db.relationship(
        User,
        secondary=enrolments,
        backref=db.backref('enrolled_trips'),
        lazy="joined"
    )

    @property
    def image_filename(self):
        return f"trip_images/{self.trip_id}.png"