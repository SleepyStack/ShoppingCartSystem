from product import Product,Physical_product,Digital_product,Grocery,Clothing,Electronics,Furniture,Beauty,Sport,Stationary,Hardware,Software,Ebook,Service,MusicProduct

class Inventory:
    inventory = {}
    product = [
    Grocery(1, "Whole Milk", 2.99, 50, "2025-08-01"),
    Grocery(2, "Brown Eggs (Dozen)", 3.49, 40, "2025-07-15"),
    Grocery(3, "Rye Bread", 1.99, 25, "2025-06-25"),
    Grocery(4, "Bananas", 0.49, 120, "2025-06-20"),

    # Clothing
    Clothing(5, "Men's T-Shirt", 12.99, 60, "L", "Black"),
    Clothing(6, "Women's Jeans", 29.99, 30, "M", "Blue"),
    Clothing(7, "Unisex Hoodie", 24.99, 20, "XL", "Grey"),
    Clothing(8, "Kid's Sneakers", 19.99, 15, "3", "Red"),

    # Electronics
    Electronics(9, "Bluetooth Headphones", 59.99, 25, "2 years"),
    Electronics(10, "Smartphone", 399.99, 10, "1 year"),
    Electronics(11, "LED Monitor 24\"", 139.99, 12, "3 years"),
    Electronics(12, "USB Flash Drive 128GB", 18.99, 100, "1 year"),

    # Furniture
    Furniture(13, "Office Desk", 109.99, 5, "Wood"),
    Furniture(14, "Dining Chair", 39.99, 20, "Metal"),
    Furniture(15, "Bookshelf", 59.99, 8, "MDF"),
    Furniture(16, "Bedside Table", 44.99, 10, "Pine Wood"),

    # Beauty
    Beauty(17, "Herbal Shampoo", 7.99, 40, "HerbalEssence"),
    Beauty(18, "Face Moisturizer", 12.49, 35, "Nivea"),
    Beauty(19, "Lipstick", 8.99, 55, "Maybelline"),
    Beauty(20, "Body Lotion", 9.99, 30, "Vaseline"),

    # Sport
    Sport(21, "Yoga Mat", 14.99, 22, "Yoga"),
    Sport(22, "Football", 19.99, 18, "Soccer"),
    Sport(23, "Tennis Racket", 29.99, 10, "Tennis"),
    Sport(24, "Boxing Gloves", 24.99, 8, "Boxing"),

    # Stationary
    Stationary(25, "A4 Notebook", 2.49, 100),
    Stationary(26, "Gel Pen (Pack of 10)", 3.99, 70),
    Stationary(27, "Highlighter Set", 4.99, 40),
    Stationary(28, "Sticky Notes", 1.99, 60),

    # Hardware
    Hardware(29, "Hammer", 11.99, 15, "Hand Tool"),
    Hardware(30, "Cordless Drill", 49.99, 8, "Power Tool"),
    Hardware(31, "Measuring Tape", 3.99, 30, "Hand Tool"),
    Hardware(32, "Adjustable Wrench", 7.99, 18, "Hand Tool"),

    # Software
    Software(33, "Photo Editor Pro", 39.99, 100, "PHOT-EDT-2025-001"),
    Software(34, "Antivirus Plus", 24.99, 150, "ANTIVIR-KEY-2025-002"),
    Software(35, "Office Suite", 59.99, 80, "OFF-SUITE-KEY-2025-003"),

    # Ebook
    Ebook(36, "Learn Python", 6.99, 200, "Jane Coder"),
    Ebook(37, "Meditation for Beginners", 4.99, 180, "Alex Peace"),
    Ebook(38, "World History", 8.49, 120, "Dr. Hist O. Rian"),

    # Service
    Service(39, "Resume Review", 14.99, 100, "30 minutes"),
    Service(40, "Online Tutoring - Math", 29.99, 50, "1 hour"),
    Service(41, "Personal Trainer Session", 39.99, 20, "1 hour"),

    # MusicProduct
    MusicProduct(42, "Shape of You", 1.29, 1000, "Ed Sheeran", "Divide", "3:53", "mp3"),
    MusicProduct(43, "Beethoven Symphony No.5", 2.49, 500, "Beethoven", "Symphonies", "7:10", "flac"),
    MusicProduct(44, "Jazz Essentials", 9.99, 300, "Various", "Jazz Essentials", "1:30:00", "mp3"),
]
    for p in product:
        inventory[p.product_id] = p