from django.core.management.base import BaseCommand
from store.models import Category, Product


class Command(BaseCommand):
    help = 'Add sample products to the shop'

    def handle(self, *args, **kwargs):
        # Clear existing products
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Create Categories
        categories_data = [
            {'name': 'Electronics', 'slug': 'electronics'},
            {'name': 'Clothing', 'slug': 'clothing'},
            {'name': 'Footwear', 'slug': 'footwear'},
            {'name': 'Accessories', 'slug': 'accessories'},
            {'name': 'Home & Living', 'slug': 'home-living'},
        ]

        categories = {}
        for cat_data in categories_data:
            cat = Category.objects.create(**cat_data)
            categories[cat_data['slug']] = cat
            self.stdout.write(f'Created category: {cat.name}')

        # Products with real image URLs from free image services
        products_data = [
            # Electronics
            {'name': 'Wireless Bluetooth Headphones', 'slug': 'wireless-headphones', 'category': 'electronics', 'description': 'High-quality wireless headphones with noise cancellation and 20-hour battery life. Perfect for music lovers.', 'price': 79.99, 'stock': 50, 'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400'},
            {'name': 'Smart Watch Pro', 'slug': 'smart-watch-pro', 'category': 'electronics', 'description': 'Feature-rich smart watch with heart rate monitor, GPS, and water resistance. Track your fitness goals.', 'price': 199.99, 'stock': 30, 'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400'},
            {'name': 'Portable Power Bank 20000mAh', 'slug': 'power-bank', 'category': 'electronics', 'description': 'High-capacity portable charger with fast charging support. Charge your devices on the go.', 'price': 39.99, 'stock': 100, 'image_url': 'https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=400'},
            {'name': 'Wireless Mouse', 'slug': 'wireless-mouse', 'category': 'electronics', 'description': 'Ergonomic wireless mouse with precision tracking. Compatible with all devices.', 'price': 24.99, 'stock': 75, 'image_url': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400'},
            {'name': 'USB-C Hub 7-in-1', 'slug': 'usb-c-hub', 'category': 'electronics', 'description': 'Multi-port adapter with HDMI, USB 3.0, SD card reader and more. Expand your connectivity.', 'price': 49.99, 'stock': 60, 'image_url': 'https://images.unsplash.com/photo-1625723044792-44de16ccb24e?w=400'},

            # Clothing
            {'name': 'Classic Cotton T-Shirt', 'slug': 'cotton-tshirt', 'category': 'clothing', 'description': 'Premium quality cotton t-shirt. Comfortable and breathable for everyday wear.', 'price': 19.99, 'stock': 200, 'image_url': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400'},
            {'name': 'Denim Jacket', 'slug': 'denim-jacket', 'category': 'clothing', 'description': 'Stylish denim jacket with modern fit. Perfect for casual outings.', 'price': 89.99, 'stock': 40, 'image_url': 'https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=400'},
            {'name': 'Casual Hoodie', 'slug': 'casual-hoodie', 'category': 'clothing', 'description': 'Soft and warm hoodie. Ideal for cold weather layering.', 'price': 49.99, 'stock': 80, 'image_url': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400'},
            {'name': 'Formal Shirt', 'slug': 'formal-shirt', 'category': 'clothing', 'description': 'Elegant formal shirt for office and events. Wrinkle-free fabric.', 'price': 34.99, 'stock': 60, 'image_url': 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=400'},
            {'name': 'Summer Dress', 'slug': 'summer-dress', 'category': 'clothing', 'description': 'Light and breezy summer dress. Perfect for casual occasions.', 'price': 44.99, 'stock': 50, 'image_url': 'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=400'},

            # Footwear
            {'name': 'Running Sneakers', 'slug': 'running-sneakers', 'category': 'footwear', 'description': 'Lightweight running shoes with cushioned sole. Perfect for athletes.', 'price': 69.99, 'stock': 70, 'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400'},
            {'name': 'Leather Formal Shoes', 'slug': 'formal-shoes', 'category': 'footwear', 'description': 'Premium leather formal shoes. Elegant and comfortable.', 'price': 119.99, 'stock': 35, 'image_url': 'https://images.unsplash.com/photo-1614252369475-531eba835eb1?w=400'},
            {'name': 'Canvas Slip-Ons', 'slug': 'canvas-slippers', 'category': 'footwear', 'description': 'Comfortable canvas slip-ons for casual wear. Easy to wear.', 'price': 29.99, 'stock': 90, 'image_url': 'https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=400'},
            {'name': 'Sports Sandals', 'slug': 'sports-sandals', 'category': 'footwear', 'description': 'Durable sports sandals with adjustable strap. Great for outdoor activities.', 'price': 34.99, 'stock': 55, 'image_url': 'https://images.unsplash.com/photo-1603487742131-4160ec999306?w=400'},
            {'name': 'Winter Boots', 'slug': 'winter-boots', 'category': 'footwear', 'description': 'Warm and sturdy winter boots. Water-resistant with good traction.', 'price': 99.99, 'stock': 25, 'image_url': 'https://images.unsplash.com/photo-1542280756-74b2f55e8ab8?w=400'},

            # Accessories
            {'name': 'Leather Wallet', 'slug': 'leather-wallet', 'category': 'accessories', 'description': 'Genuine leather wallet with multiple card slots. Slim and stylish.', 'price': 39.99, 'stock': 85, 'image_url': 'https://images.unsplash.com/photo-1627123424574-724758594e93?w=400'},
            {'name': 'Sunglasses', 'slug': 'sunglasses', 'category': 'accessories', 'description': 'UV protection sunglasses with modern design. Protect your eyes in style.', 'price': 24.99, 'stock': 120, 'image_url': 'https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=400'},
            {'name': 'Leather Belt', 'slug': 'leather-belt', 'category': 'accessories', 'description': 'Classic leather belt. Adjustable buckle for perfect fit.', 'price': 29.99, 'stock': 70, 'image_url': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400'},
            {'name': 'Backpack', 'slug': 'backpack', 'category': 'accessories', 'description': 'Spacious backpack with laptop compartment. Water-resistant material.', 'price': 54.99, 'stock': 45, 'image_url': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400'},
            {'name': 'Watch', 'slug': 'wrist-watch', 'category': 'accessories', 'description': 'Elegant wrist watch with stainless steel band. Water-resistant.', 'price': 149.99, 'stock': 30, 'image_url': 'https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=400'},

            # Home & Living
            {'name': 'Bed Sheet Set', 'slug': 'bed-sheet-set', 'category': 'home-living', 'description': 'Soft and comfortable bed sheet set. 100% cotton. Machine washable.', 'price': 49.99, 'stock': 65, 'image_url': 'https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=400'},
            {'name': 'Cushion Cover Set', 'slug': 'cushion-covers', 'category': 'home-living', 'description': 'Set of 4 decorative cushion covers. Adds style to your living room.', 'price': 29.99, 'stock': 80, 'image_url': 'https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?w=400'},
            {'name': 'Table Lamp', 'slug': 'table-lamp', 'category': 'home-living', 'description': 'Modern table lamp with warm LED light. Perfect for bedside or desk.', 'price': 44.99, 'stock': 40, 'image_url': 'https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=400'},
            {'name': 'Wall Clock', 'slug': 'wall-clock', 'category': 'home-living', 'description': 'Silent wall clock with modern design. Battery operated.', 'price': 19.99, 'stock': 95, 'image_url': 'https://images.unsplash.com/photo-1563861826100-9cb868fdbe1c?w=400'},
            {'name': 'Plant Pot Set', 'slug': 'plant-pots', 'category': 'home-living', 'description': 'Set of 3 decorative plant pots. Perfect for indoor plants.', 'price': 34.99, 'stock': 55, 'image_url': 'https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=400'},
        ]

        for prod_data in products_data:
            cat_slug = prod_data.pop('category')
            image_url = prod_data.pop('image_url', None)
            prod_data['category'] = categories[cat_slug]
            product = Product.objects.create(**prod_data)
            
            # Save the image URL to the product
            if image_url:
                product.image_url = image_url
                product.save()
            
            self.stdout.write(f'Created product: {prod_data["name"]}')

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully added {len(products_data)} products in {len(categories_data)} categories!'))
        self.stdout.write(self.style.SUCCESS('Image URLs have been saved to the database!'))
