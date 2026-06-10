import json
import random

# ============================================
# CẤU HÌNH
# ============================================
SO_LUONG_TU_KHOA = 10000

# ============================================
# CHỦ ĐỀ BẰNG TIẾNG VIỆT
# ============================================
chu_de = {
    "toan_hoc": {
        "chu_de": ["toán học", "giải tích", "đại số", "hình học", "lượng giác", 
                   "thống kê", "xác suất", "đạo hàm", "tích phân", "giới hạn", 
                   "hàm số", "ma trận", "vectơ", "phương trình", "logarit", 
                   "phân số", "phần trăm", "căn bậc hai", "lũy thừa", "đa thức", 
                   "số phức", "phương trình vi phân", "đại số tuyến tính",
                   "lượng giác cầu", "giải tích vectơ", "tô pô", "lý thuyết số"]
    },
    "vat_ly": {
        "chu_de": ["vật lý", "cơ học", "nhiệt động lực học", "điện từ học", "quang học", 
                   "âm học", "động học", "động lực học", "chất lưu", "vật lý lượng tử", 
                   "thuyết tương đối", "năng lượng", "công", "công suất", "chuyển động", 
                   "lực", "trọng lực", "điện", "từ tính", "sóng",
                   "vật lý thiên văn", "vũ trụ học", "vật lý hạt nhân", "vật lý phân tử"]
    },
    "hoa_hoc": {
        "chu_de": ["hóa học", "hóa hữu cơ", "hóa vô cơ", "hóa phân tích", 
                   "hóa sinh", "phản ứng hóa học", "cân bằng", "hóa học lượng pháp", 
                   "bảng tuần hoàn", "liên kết hóa học", "phân tử", "nguyên tử", 
                   "hợp chất hóa học", "axit", "bazơ", "ph", "dung dịch", 
                   "khí", "nhiệt hóa học", "hóa học lượng tử", "hóa điện"]
    },
    "sinh_vat_hoc": {
        "chu_de": ["sinh vật học", "sinh học tế bào", "sinh học phân tử", "di truyền học", 
                   "giải phẫu học", "sinh lý học", "sinh thái học", "tiến hóa", "thực vật học", 
                   "động vật học", "vi sinh vật học", "adn", "arn", "protein", "enzym", 
                   "trao đổi chất", "tế bào", "mô", "cơ quan", "hệ thống cơ thể",
                   "khoa học thần kinh", "miễn dịch học", "phôi học"]
    },
    "lap_trinh": {
        "chu_de": ["lập trình", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "tri_tue_nhan_tao": {
        "chu_de_dac_biet": ["học máy", "học sâu", "gpt", "llm"],
        "chu_de": ["trí tuệ nhân tạo", "mạng nơ-ron", "xử lý ngôn ngữ tự nhiên", 
                   "thị giác máy tính", "chatbot", "bộ biến đổi", "tự động hóa",
                   "học máy", "học sâu", "xử lý ngôn ngữ tự nhiên", "thị giác máy tính"]
    },
    "an_ninh_mang": {
        "chu_de": ["an ninh mạng", "tin tặc đạo đức", "tường lửa", "mã hóa", 
                   "an toàn thông tin", "kiểm tra thâm nhập", "phần mềm độc hại", "phần mềm tống tiền", 
                   "lừa đảo", "kỹ thuật xã hội", "mật mã học", "an ninh mạng",
                   "an ninh web", "an ninh di động", "tin tặc đạo đức"]
    },
    "nau_an": {
        "chu_de": ["nấu ăn", "công thức dễ", "món tráng miệng", "làm bánh", "bánh ngọt", 
                   "ẩm thực Mexico", "ẩm thực Ý", "ẩm thực Tây Ban Nha", "đồ uống", 
                   "cocktail", "cocktail", "kết hợp rượu vang", "rượu vang", "bia thủ công",
                   "ẩm thực phân tử", "nấu ăn chay", "nấu ăn thuần chay"]
    },
    "the_thao": {
        "chu_de": ["thể thao", "bóng đá", "bóng rổ", "quần vợt", "bơi lội", "chạy bộ", 
                   "thể hình", "phòng gym", "yoga", "pilates", "crossfit", "dinh dưỡng thể thao",
                   "tập luyện chức năng", "tập thể dục thân thể", "quyền anh", "võ thuật"]
    },
    "kinh_doanh": {
        "chu_de": ["kinh doanh", "khởi nghiệp", "công ty khởi nghiệp", "tiếp thị kỹ thuật số", "bán hàng", 
                   "tài chính cá nhân", "đầu tư", "kinh doanh trực tuyến", "thương mại điện tử", 
                   "hậu cần", "lãnh đạo", "quản lý doanh nghiệp", "nguồn nhân lực",
                   "dịch vụ khách hàng", "xây dựng thương hiệu", "seo", "sem", "tiếp thị qua email"]
    }
}

# ============================================
# TIỀN TỐ
# ============================================
tien_to = [
    "cách học", "cách thành thạo", "hướng dẫn đầy đủ về", "hướng dẫn về", "khóa học về",
    "thành thạo", "hiểu", "thực hành", "giải quyết vấn đề về", "bài tập về",
    "giới thiệu về", "khái niệm cơ bản về", "sách hướng dẫn về", "lý thuyết về",
    "ví dụ về", "nguyên tắc cơ bản của", "mẹo học", "tài liệu học tập",
    "bài học về", "bài học về", "cách cải thiện trong", "cách sử dụng"
]

# ============================================
# HẬU TỐ
# ============================================
hau_to = [
    "cho người mới bắt đầu", "trung cấp", "nâng cao", "chuyên nghiệp", "hoàn chỉnh",
    "dễ", "nhanh", "cho người mới bắt đầu", "từ đầu", "từng bước",
    "có bài tập", "trực tuyến", "miễn phí", "được chứng nhận", "cấp đại học",
    "cho trẻ em", "cho người lớn", "chuyên sâu", "thực tế", "lý thuyết"
]

# ============================================
# CÂU HỎI
# ============================================
cau_hoi = [
    "là gì", "hoạt động như thế nào", "dùng để làm gì", "học ở đâu",
    "khi nào sử dụng", "tại sao quan trọng", "lợi ích là gì",
    "mất bao lâu để học", "cần gì để học"
]

# ============================================
# TẠO TỪ KHÓA
# ============================================
tu_khoa = set()

print("🔄 Đang tạo từ khóa tiếng Việt...")

for tien in tien_to:
    for cat_data in chu_de.values():
        for chu in cat_data["chu_de"]:
            tu_khoa.add(f"{tien} {chu}")
        for chu_dac_biet in cat_data.get("chu_de_dac_biet", []):
            tu_khoa.add(f"{tien} {chu_dac_biet}")

for hau in hau_to:
    for cat_data in chu_de.values():
        for chu in cat_data["chu_de"][:15]:
            tu_khoa.add(f"{chu} {hau}")
        for chu_dac_biet in cat_data.get("chu_de_dac_biet", []):
            tu_khoa.add(f"{chu_dac_biet} {hau}")

for cau in cau_hoi:
    for cat_data in chu_de.values():
        for chu in cat_data["chu_de"][:15]:
            tu_khoa.add(f"{cau} {chu}")
        for chu_dac_biet in cat_data.get("chu_de_dac_biet", []):
            tu_khoa.add(f"{cau} {chu_dac_biet}")

dong_tu = ["học", "thành thạo", "thực hành", "nghiên cứu", "hiểu", "áp dụng"]
for dt in dong_tu:
    for cat_data in chu_de.values():
        for chu in cat_data["chu_de"][:15]:
            tu_khoa.add(f"{dt} {chu}")

for cat_data in chu_de.values():
    tat_ca_chu_de = cat_data["chu_de"] + cat_data.get("chu_de_dac_biet", [])
    if len(tat_ca_chu_de) >= 2:
        for _ in range(min(30, len(tat_ca_chu_de) * 3)):
            chu1, chu2 = random.sample(tat_ca_chu_de, 2)
            tu_khoa.add(f"sự khác biệt giữa {chu1} và {chu2}")
            tu_khoa.add(f"{chu1} vs {chu2}")
            tu_khoa.add(f"so sánh {chu1} và {chu2}")

for cat_data in chu_de.values():
    for chu in cat_data["chu_de"][:10]:
        tu_khoa.add(f"lỗi thường gặp trong {chu}")
        tu_khoa.add(f"cách tránh lỗi trong {chu}")
        tu_khoa.add(f"giải pháp cho vấn đề {chu}")

trinh_do = ["cơ bản", "trung cấp", "nâng cao", "chuyên nghiệp", "chuyên sâu"]
for td in trinh_do:
    for cat_data in chu_de.values():
        for chu in cat_data["chu_de"][:12]:
            tu_khoa.add(f"khóa học {td} về {chu}")
            tu_khoa.add(f"bài học {chu} trình độ {td}")

for cat_data in chu_de.values():
    for chu in cat_data["chu_de"][:10]:
        tu_khoa.add(f"chứng chỉ về {chu}")
        tu_khoa.add(f"kỳ thi về {chu}")
        tu_khoa.add(f"sách về {chu}")
        tu_khoa.add(f"video về {chu}")

for cat_data in chu_de.values():
    for chu in cat_data["chu_de"][:10]:
        tu_khoa.add(f"mẹo cho {chu}")
        tu_khoa.add(f"lời khuyên để cải thiện trong {chu}")

for i in range(1, 2000):
    cat_name = random.choice(list(chu_de.keys()))
    chu = random.choice(chu_de[cat_name]["chu_de"])
    tu_khoa.add(f"{chu} bài {i}")
    tu_khoa.add(f"{chu} chương {i}")
    tu_khoa.add(f"{chu} đơn vị {i}")

# ============================================
# GIỚI HẠN
# ============================================
danh_sach_tu_khoa = sorted(list(tu_khoa))
random.shuffle(danh_sach_tu_khoa)

if len(danh_sach_tu_khoa) < SO_LUONG_TU_KHOA:
    print(f"⚠ Chỉ tạo được {len(danh_sach_tu_khoa)} từ khóa. Đang lặp lại một số để đạt {SO_LUONG_TU_KHOA}...")
    while len(danh_sach_tu_khoa) < SO_LUONG_TU_KHOA:
        danh_sach_tu_khoa.extend(danh_sach_tu_khoa[:min(1000, SO_LUONG_TU_KHOA - len(danh_sach_tu_khoa))])

tu_khoa_cuoi = danh_sach_tu_khoa[:SO_LUONG_TU_KHOA]
random.shuffle(tu_khoa_cuoi)

# ============================================
# LƯU
# ============================================
with open('keywords/vi.json', 'w', encoding='utf-8') as f:
    json.dump(tu_khoa_cuoi, f, indent=2, ensure_ascii=False)

# ============================================
# BÁO CÁO
# ============================================
print(f"\n✅ Đã tạo {len(tu_khoa_cuoi)} từ khóa tiếng Việt")
print(f"📁 Đã lưu tại: keywords/vi.json")
print(f"\n📊 Xem trước (30 từ khóa đầu tiên):")
for i, kw in enumerate(tu_khoa_cuoi[:30]):
    print(f"   {i+1}. {kw}")
