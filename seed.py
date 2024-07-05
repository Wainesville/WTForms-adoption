from models import Pet, db
from app import app
app.app_context().push()

db.drop_all()
db.create_all()

goose = Pet(id="1", name="Goose", species="Cat", photo_url="https://assets1.ignimgs.com/2019/03/07/goosethecat-blogroll-1551733410083-1280w-1551990377836_160w.jpg?width=1280", age="30", notes="Actually a Flarken", available=False)
bats = Pet(id="2", name="Bats", species="Dog", photo_url="https://cdn.marvel.com/content/1x/strange_pg_6_bats_resized.jpg", age="150", notes="Ghost Dog", available=False)
lockjaw = Pet(id="3", name="Lockjaw", species="Dog", photo_url="https://cdn.marvel.com/content/1x/065lkj_com_crd_01.jpg", age="300", notes="Teleporting Inhuman Dog", available=True)
lucky = Pet(id="5", name="Lucky", species="Dog", photo_url="https://cdn.marvel.com/content/1x/marvel_unleashed_pizza_dog.jpg", age="4", notes="Has one eye, eats Pizza", available=True)
alpine = Pet(id="6", name="Apline", species="Cat", photo_url="https://s3.amazonaws.com/comicgeeks/characters/avatars/16275.jpg?t=1614654384", age="10", notes="Super chill", available=True)

db.session.add_all([goose,bats,lockjaw,lucky,alpine])

db.session.commit()


