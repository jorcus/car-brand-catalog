from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Brand, Base, User

engine = create_engine('sqlite:///brandmenuwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


brand1 = Brand(user_id=1, name="Mercedes",
                         photo="http://www.hdwallpaper.nu/wp-content/uploads/2015/12/Mercedes_Logo_10.jpg",
                         description="A Star Is Born: Origin of the Mercedes-Benz Name and Logo. Gottlieb Daimler originally founded Daimler-Motoren-Gesellschaft (DMG) in 1890, while Carl Benz began Benz & Cie in 1883.")

session.add(brand1)
session.commit()

brand1 = Brand(user_id=1, name="BMW",
                         photo="http://i826.photobucket.com/albums/zz190/tpku_2b4/Wallpaper/25d227f3.jpg",
                         description='BMW stands for "Bayerische Motoren Werke AG" which translated into English is "Bavarian Motor Works" based in Munich, Bavaria in Germany.')

session.add(brand1)
session.commit()
brand1 = Brand(user_id=1, name="Audi",
                         photo="http://www.car-brand-names.com/wp-content/uploads/2015/03/Audi-emblem.jpg",
                         description='The company name is based on the Latin translation of the surname of the founder, August Horch. "Horch", meaning "listen" in German, becomes "audi" in Latin. The four rings of the Audi logo each represent one of four car companies that banded together to create Audi predecessor company, Auto Union.')

session.add(brand1)
session.commit()

brand1 = Brand(user_id=1, name="McLaren",
                         photo="http://freevector.co/wp-content/uploads/2012/07/mclaren.png",
                         description="McLaren Racing Limited, competing as McLaren Honda, is a British Formula One team based at the McLaren Technology Centre, Woking, Surrey, England.")

session.add(brand1)
session.commit()

brand1 = Brand(user_id=1, name="Tesla",
                         photo="https://www.creativecrash.com/system/photos/000/177/135/177135/big/Tesla_1.jpg?1323236895",
                         description="Tesla's engineers first designed a powertrain for a sports car built around an AC induction motor, patented in 1888 by Nikola Tesla, the inventor who inspired the company's name. The resulting Tesla Roadster was launched in 2008")

session.add(brand1)
session.commit()

brand1 = Brand(user_id=1, name="Lamborghini",
                         photo="http://aboutmyfavcars.weebly.com/uploads/2/3/5/9/23590822/8822791_orig.jpg",
                         description="The Lamborghini logo shows a bull or Taurus that is the brand founder's zodiac sign. Ferruccio Lamborghini was extremely interested in Spanish bullfighting sport that is also shown in the logo. Bullfighting is the main part of Lamborghini's style. Furthermore many Lamborghini cars are called as famous bulls.")

session.add(brand1)
session.commit()

print "added car brand!"
