from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CatalogItem, User

engine = create_engine('sqlite:///itemcatalogwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you calling
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Example John", email="abcd@example.com", picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


# Catalog for Zara
category1 = Category(user_id=1, name="ZARA")

session.add(category1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="OVERSIZED MILITARY PARKA", description="Oversized military parka with hood, zip and snap button fastening ",
                     price="$159.00", season="Winter", category=category1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="PLUSH BERMUDA SHORTS", description="Plush jersey bermuda shorts with elastic drawstring waistband, off-seam pockets and back pockets",
                     price="$35.90", season="Summer", category=category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="RIPPED DENIM BERMUDA SHORTS", description="Ripped denim bermuda shorts with zip and button fastening and five pockets",
                     price="$45.90", season="Summer", category=category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="STREET SWEATSHIRT", description="Sweatshirt featuring adjustable hood with cord and short sleeves",
                     price="$45.90", season="Autumn", category=category1)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="CHECKED BLAZER", description="Classic, checked blazer with pointed lapels and button fastening",
                     price="$159.00", season="spring", category=category1)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="COMBINED LEATHER SNEAKERS", description="Leather sneakers with laces with a black coloured soles",
                     price="$89.90", season="Spring", category=category1)

session.add(catalogItem5)
session.commit()

catalogItem6 = CatalogItem(user_id=1, name="HOUNDSTOOTH BLAZER", description="Printed blazer with stretch and classic pointed lapels",
                     price="$159.00", season="Spring", category=category1)

session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(user_id=1, name="OXFORD SHIRT WITH MANDARIN COLLAR", description="Relaxed fit Oxford shirt with long sleeves",
                     price="$35.90", season="Summer", category=category1)

session.add(catalogItem7)
session.commit()

catalogItem8 = CatalogItem(user_id=1, name="OVERSIZED QUILTED PARKA", description="Oversized quilted parka with adjustable hood",
                     price="$129.00", season="Winter", category=category1)

session.add(catalogItem8)
session.commit()


# catalog for RALPH LAUREN
category2 = Category(user_id=1, name="RALPH LAUREN")

session.add(category2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="PACKABLE WINDBREAKER", description="water-repellent fabric and lightweight fill",
                     price="$225.50", season="Winter", category=category2)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(
    user_id=1, name="CLASSIC FIT MESH POLO SHIRT", description=" Ralph Lauren debuted his original Polo shirt in 1972, and today the iconic design is offered in a wide array of colors and fits", price="$85", season="Summer", category=category2)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="SULLIVAN SLIM FIT JEAN", description="In lightweight stretch denim, these Slim Fit jeans are garment-dyed to give them a broken-in look and feel ",
                     price="125.00", season="Spring", category=category2)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="LEATHER DRIVING GLOVES ", description="Our supple Leather Driving Gloves are designed with intricate perforations and snapped tab closures that ensure a comfortable, no-slip fit. ",
                     price="80.00", season="Winter", category=category2)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="SULLIVAN SLIM STRETCH JEAN", description="jeans will take you from the office to the weekend",
                     price="125.00", season="Summer", category=category2)

session.add(catalogItem5)
session.commit()

catalogItem6 = CatalogItem(user_id=1, name="KEYHOLE-BRIDGE SUNGLASSES", description="A nod to the iconic Ivy League style that continually inspires Polo",
                     price="199.00", season="Summer", category=category2)

session.add(catalogItem6)
session.commit()


# catalog for WINNERS
category1 = Category(user_id=1, name="WINNERS")

session.add(category1)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Short sleeve shirt", description="Polo made brand",
                     price="$19.99", season="Summer", category=category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Bomber jacket", description="Made for the summer",
                     price="$49.99", season="Summer", category=category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Gyoza Joggers", description="Sportswear as streetwear is a trend worth trying",
                     price="$19.99", season="Spring", category=category1)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Suede shoe", description="Comfortable but stylish",
                     price="$49.99", season="Spring", category=category1)

session.add(catalogItem4)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Teddy Running Shoes", description="Beat Usin Bolt",
                     price="$39.99", season="Summer", category=category1)

session.add(catalogItem2)
session.commit()


# catalog for ABERCROMBIE & FINCH
category1 = Category(user_id=1, name="ABERCROMBIE & FINCH ")

session.add(category1)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="STRAIGHT JEANS", description="Straight wired, made for the cold season",
                     price="$42", season="Winter", category=category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="ATHLETIC SLIM CHINO PANTS", description="Sleek and fit",
                     price="$74", season="Spring", category=category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="PULLOVER HOODED PUFFER", description="100% nylon packable hooded puffer in pullover silhouette with down fill, water-resistant fabric, front zipper, adjustable bungee",
                     price="$150", season="Winter", category=category1)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="NEW BALANCE 420 RE-ENGINEERED SNEAKERS", description="The iconic 420 gets a modern revision with comfort features like a classic leather upper and a lightweight REVlite midsole",
                     price="$6.95", season="Summer", category=category1)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="HERRINGBONE POPOVER SHIRT", description="From professional to casual",
                     price="$200", season="Fall", category=category1)

session.add(catalogItem5)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="GOLDEN BEAR SUEDE BOMBER JACKET", description="Everything you desire in one",
                     price="$640", season="Fall", category=category1)

session.add(catalogItem2)
session.commit()


# catalog for AMERICAN EAGLE OUTFITTERS
category1 = Category(user_id=1, name="AMERICAN EAGLE OUTFITTERS ")

session.add(category1)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="EASTLAND SENECA CAMP MOC CHUKKA BOOT", description="classic five-eye chukka features hand sewn moccasin construction, memory foam insole and shock absorbing natural rubber outsole",
                     price="$120", season="Fall", category=category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="FLEECE JOGGERS", description="Classic fleece joggers with a soft cotton blend, drawstrings at waistband and side-entry pockets",
                     price="$38.40", season="Fall", category=category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="AEO FLEX CREW T-SHIRT", description="Super soft cotton blend jersey",
                     price="$25.12", season="Fall", category=category1)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="AEO EXTREME FLEX ORIGINAL STRAIGHT JEAN",
                     description="Extreme Flex moves with you for comfort that feels better than the rest", price="$62.89", season="Winter", category=category1)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="AEO OVERSIZED DESTROYED FLANNEL SHIRT", description="Some styles feature back patches or embroidery",
                     price="$62.89", season="Fall", category=category1)

session.add(catalogItem5)
session.commit()


# catalog for TOMMY HILFIGER
category1 = Category(user_id=1, name="TOMMY HILFIGER")

session.add(category1)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="SLIM FIT LUXURY PIQUE POLO", description="Tommy Hilfiger men's polo. What we do best-the iconic polo in pique cotton, refreshed in our modern, slim fit. ",
                     price="$69.50", season="Fall", category=category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="CREWNECK SWEATSHIRT", description="Tommy Hilfiger men's fleece. The old-school gym sweatshirt gets an update in our heavyweight spun cotton",
                     price="$99.50", season="Fall", category=category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="VARSITY CARDIGAN", description="Tommy Hilfiger men's sweater. Our take on a varsity jacket, in cardigan form.",
                     price="$149.50", season="Summer", category=category1)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="AIRSPUN INDIGO SWEATSHIRT", description="Tommy Hilfiger men's fleece. A sleek look in double-face cotton, this sweatshirt is light as air in indigo while keeping your clean lines in check",
                     price="$6.75", season="Summer", category=category1)

session.add(catalogItem4)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="TAILORED COLLECTION SLIM FIT SHIRT", description="Tommy Hilfiger men's shirt. Our premium cotton shirt is cut to perfection in a bold stripe. Part of our Tailored Collection. ",
                     price="$99.50", season="Fall", category=category1)

session.add(catalogItem2)
session.commit()


# catalog for GUCCI
category1 = Category(user_id=1, name="GUCCI ")

session.add(category1)
session.commit()

catalogItem9 = CatalogItem(user_id=1, name="Embroidered wool knitted sweater", description="A constant fascination with the world of nature permeates Gucci's collections and is mirrored in the ornate details decorating the House's creations",
                     price="$1650.00", season="Fall", category=category1)

session.add(catalogItem9)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Wool sweater with Angry Cat and heart", description="Alessandro Michele continues to introduce contemporary codes representative of the House",
                     price="$1315.00", season="Winter", category=category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Horsebit leather slipper", description="An evolution of the Horsebit slipper, designed with a wide rounded toe in leather",
                     price="$1495.00", season="Fall", category=category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Princetown leather slipper with Double G", description="The Princetown fur-lined leather slipper is completed with a leather strap across the front with House Web stripe and Double G hardware",
                     price="$1190", season="Summer", category=category1)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Monaco geometric pattern wool suit", description="The Monaco suit is designed with a slim, tapered silhouette and soft, rounded shoulders",
                     price="$3820", season="Fall", category=category1)

session.add(catalogItem4)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Wool scarf with wolf jacquard", description="The wolf is depicted leaping across the wool scarf. In contrast colors",
                     price="$320.00", season="Fall", category=category1)

session.add(catalogItem2)
session.commit()

catalogItem10 = CatalogItem(user_id=1, name="Check wool cashmere scarf with wolf", description="A wool cashmere scarf with a check pattern",
                      price="$1045", season="Winter", category=category1)

session.add(catalogItem10)
session.commit()


# catalog for Under Armour
category1 = Category(user_id=1, name="Under Armour ")

session.add(category1)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Mens Track Jacket", description="Tight but relaxing",
                     price="$5.95", season="Fall", category=category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="UA Threadborne Slingwrap", description="The Threadborne Slingwrap fits like a sock and easily goes from the run right into everyday wear",
                     price="$129.99.99", season="Fall", category=category1)

session.add(catalogItem2)
session.commit()

# catalog for GAP
category1 = Category(user_id=1, name="GAP")
session.add(category1)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Solid pique polo", description="Straight, easy fit.",
                     price="$100", season="Summer", category=category1)

session.add(catalogItem1)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Guanciale Chawanmushi", description="Hits at the hip",
                     price="$50.00", season="Winter", category=category1)

session.add(catalogItem1)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="French terry moto joggers", description="Relaxed through the leg",
                     price="$45.25", season="Winter", category=category1)

session.add(catalogItem1)
session.commit()


print "added catalog items!"
