from product import (
    Product, Physical_product, Digital_product, Grocery, Clothing, Electronics, Furniture,
    Beauty, Sport, Stationary, Hardware, Software, Ebook, Service, MusicProduct
)

class Inventory:
    inventory = {}

    product = [
        # Grocery (product_id: Any, name: str, price: float, quantity: int, expiration_date: str) -> Grocery

        Grocery(1, "Whole Milk", 2.99, 50, "2025-08-01"),
        Grocery(2, "Brown Eggs (Dozen)", 3.49, 40, "2025-07-15"),
        Grocery(3, "Rye Bread", 1.99, 25, "2025-06-25"),
        Grocery(4, "Bananas", 0.49, 120, "2025-06-20"),
        Grocery(5, "Potato", 0.25, 500, "2025-07-10"),
        Grocery(6, "Tomato", 0.30, 100, "2025-06-30"),
        Grocery(7, "Spinach Bunch", 1.50, 60, "2025-06-22"),
        Grocery(8, "Chicken Breast (1 lb)", 4.99, 40, "2025-06-21"),
        Grocery(9, "Orange Juice", 3.99, 70, "2025-07-05"),
        Grocery(10, "Apples (Bag)", 3.20, 80, "2025-06-28"),

        # Clothing (self, product_id, name: str, price: float, quantity: int, size: str, color: str):

        Clothing(11, "Men's T-Shirt", 12.99, 60, "L", "Black"),
        Clothing(12, "Women's Jeans", 29.99, 30, "M", "Blue"),
        Clothing(13, "Unisex Hoodie", 24.99, 20, "XL", "Grey"),
        Clothing(14, "Kid's Sneakers", 19.99, 15, "L", "Red"),
        Clothing(15, "Women's Jacket", 49.99, 10, "M", "Beige"),
        Clothing(16, "Men's Shorts", 15.99, 25, "L", "Navy"),
        Clothing(17, "Children's Raincoat", 17.99, 18, "S", "Yellow"),
        Clothing(18, "Men's Socks (5-pack)", 7.99, 40, "M", "White"),

        # Electronics (product_id: Any, name: str, price: float, quantity: int, warranty_period: str) 

        Electronics(19, "Bluetooth Headphones", 59.99, 25, "2 years"),
        Electronics(20, "Smartphone", 399.99, 10, "1 year"),
        Electronics(21, "LED Monitor 32inch", 139.99, 12, "3 years"),
        Electronics(22, "USB Flash Drive 128GB", 18.99, 100, "1 year"),
        Electronics(23, "Wireless Mouse", 14.99, 60, "2 years"),
        Electronics(24, "Laptop", 799.99, 8, "1 year"),
        Electronics(25, "Bluetooth Speaker", 34.99, 20, "1 year"),
        Electronics(26, "Smartwatch", 149.99, 15, "1 year"),

        # Furniture (self, product_id, name: str, price: float, quantity: int, material: str):

        Furniture(27, "Office Desk", 109.99, 5, "Wood"),
        Furniture(28, "Dining Chair", 39.99, 20, "Metal"),
        Furniture(29, "Bookshelf", 59.99, 8, "MDF"),
        Furniture(30, "Bedside Table", 44.99, 10, "Pine Wood"),
        Furniture(31, "Sofa", 299.99, 2, "Leather"),
        Furniture(32, "Coffee Table", 79.99, 4, "Glass"),
        Furniture(33, "Wardrobe", 259.99, 3, "Oak"),
        Furniture(34, "Bar Stool", 54.99, 7, "Steel"),

        # Beauty (self, product_id, name: str, price: float, quantity: int, brand: str):

        Beauty(35, "Herbal Shampoo", 7.99, 40, "HerbalEssence"),
        Beauty(36, "Face Moisturizer", 12.49, 35, "Nivea"),
        Beauty(37, "Lipstick", 8.99, 55, "Maybelline"),
        Beauty(38, "Body Lotion", 9.99, 30, "Vaseline"),
        Beauty(39, "Nail Polish", 5.99, 25, "Lakme"),
        Beauty(40, "Sunscreen SPF50", 14.99, 28, "Lotus"),
        Beauty(41, "Hair Oil", 6.49, 32, "Parachute"),
        Beauty(42, "Face Wash", 4.99, 40, "Clean&Clear"),

        # Sport (self, product_id, name: str, price: float, quantity: int, type_of_sport: str):

        Sport(43, "Yoga Mat", 14.99, 22, "Yoga"),
        Sport(44, "Football", 19.99, 18, "Soccer"),
        Sport(45, "Tennis Racket", 29.99, 10, "Tennis"),
        Sport(46, "Boxing Gloves", 24.99, 8, "Boxing"),
        Sport(47, "Basketball", 21.99, 12, "Basketball"),
        Sport(48, "Skipping Rope", 5.99, 25, "Fitness"),
        Sport(49, "Cricket Bat", 34.99, 7, "Cricket"),
        Sport(50, "Swim Goggles", 9.99, 30, "Swimming"),

        # Stationary (self, product_id, name: str, price: float, quantity: int,):

        Stationary(51, "A4 Notebook", 2.49, 100),
        Stationary(52, "Gel Pen (Pack of 10)", 3.99, 70),
        Stationary(53, "Highlighter Set", 4.99, 40),
        Stationary(54, "Sticky Notes", 1.99, 60),
        Stationary(55, "Pencil Box", 5.49, 35),
        Stationary(56, "Drawing Book", 3.99, 50),
        Stationary(57, "Ballpoint Pen", 1.49, 90),
        Stationary(58, "Eraser Pack", 0.99, 120),

        # Hardware (self,product_id, name: str, price: float, quantity: int, type_of_hardware: str):
        
        Hardware(59, "Hammer", 11.99, 15, "Hand Tool"),
        Hardware(60, "Cordless Drill", 49.99, 8, "Power Tool"),
        Hardware(61, "Measuring Tape", 3.99, 30, "Hand Tool"),
        Hardware(62, "Adjustable Wrench", 7.99, 18, "Hand Tool"),
        Hardware(63, "Screwdriver Set", 9.99, 25, "Hand Tool"),
        Hardware(64, "Pliers", 5.99, 20, "Hand Tool"),
        Hardware(65, "Electric Saw", 59.99, 4, "Power Tool"),
        Hardware(66, "Level Tool", 8.49, 16, "Hand Tool"),

        # Software (self, product_id, name: str, price: float, quantity: int, license_key: str):

        Software(67, "Photo Editor Pro", 39.99, 100, "PHOT-EDT-2025-001"),
        Software(68, "Antivirus Plus", 24.99, 150, "ANTIVIR-KEY-2025-002"),
        Software(69, "Office Suite", 59.99, 80, "OFF-SUITE-KEY-2025-003"),
        Software(70, "Music Studio", 79.99, 50, "MUSIC-STUDIO-2025-004"),
        Software(71, "Video Editor Deluxe", 69.99, 60, "VIDEO-EDIT-2025-005"),
        Software(72, "Password Manager", 19.99, 110, "PASS-MAN-2025-006"),

        # Ebook (self, product_id, name: str, price: float, quantity: int, author: str):

        Ebook(73, "Learn Python", 6.99, 200, "Jane Coder"),
        Ebook(74, "Meditation for Beginners", 4.99, 180, "Alex Peace"),
        Ebook(75, "World History", 8.49, 120, "Dr. Hist O. Rian"),
        Ebook(76, "Quantum Physics", 10.99, 90, "Max Planck"),
        Ebook(77, "Creative Writing", 5.99, 150, "Ann Author"),
        Ebook(78, "Startup Stories", 7.99, 130, "Biz Founder"),

        # Service (self, product_id, name: str, price: float, quantity: int, duration: str):
        Service(79, "Resume Review", 14.99, 100, "30 minutes"),
        Service(80, "Online Tutoring - Math", 29.99, 50, "1 hour"),
        Service(81, "Personal Trainer Session", 39.99, 20, "1 hour"),
        Service(82, "Career Counseling", 24.99, 30, "45 minutes"),
        Service(83, "Guitar Lesson", 19.99, 25, "1 hour"),
        Service(84, "Pet Walking", 9.99, 40, "30 minutes"),

        # MusicProduct (self, product_id, name: str, price: float, quantity: int, artist: str, album: str, duration: str, audio_format: str):

        MusicProduct(85, "Shape of You", 1.29, 1000, "Ed Sheeran", "Divide", "3:53", "mp3"),
        MusicProduct(86, "Beethoven Symphony No.5", 2.49, 500, "Beethoven", "Symphonies", "7:10", "flac"),
        MusicProduct(87, "Jazz Essentials", 9.99, 300, "Various", "Jazz Essentials", "1:30:00", "mp3"),
        MusicProduct(88, "Classic Rock Hits", 7.99, 400, "Various", "Rock Anthems", "2:00:00", "mp3"),
        MusicProduct(89, "Pop Party", 5.99, 600, "Various", "Top Pop", "1:10:00", "mp3"),
        MusicProduct(90, "Chill Vibes", 4.99, 550, "Various", "Relaxation", "1:00:00", "aac"),
              ]

    for p in product:
        inventory[p.product_id] = p
