# Contoh data produk rekomendasi
rekomendasi_produk = [
    {"product_id": 2, "product_title": "Contoh Produk 1", "score": 4.5},
    {"product_id": 3, "product_title": "Contoh Produk 2", "score": 4.2},
    {"product_id": 4, "product_title": "Contoh Produk 3", "score": 4.0}
    # ... tambahkan rekomendasi lainnya sesuai kebutuhan
]

# Contoh data produk utama
produk_utama = {
    "ID": 1,
    "brand_title": "Lenovo (IdeaPad Slim D330 Flex)",
    "rekomen": rekomendasi_produk
}

# Konversi ke format JSON
import json

output_json = json.dumps(produk_utama, indent=2)

# Tampilkan output
print(output_json)
