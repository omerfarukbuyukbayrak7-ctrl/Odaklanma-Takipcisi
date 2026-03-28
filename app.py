import streamlit as st
import time

# Sayfa Ayarları
st.set_page_config(page_title="DeepWork Pro", page_icon="🚀", layout="centered")

# Yan Menü (Sidebar)
with st.sidebar:
    st.title("⚙️ Ayarlar")
    st.write("Kullanıcı: Ömer Faruk")
    theme = st.selectbox("Tema Seçin", ["Aydınlık", "Karanlık (Yakında)"])
    st.divider()
    st.info("Bu uygulama odaklanmanı artırmak için tasarlandı.")

# Ana Başlık
st.title("🚀 DeepWork Odaklanma Takipçisi")
st.markdown("---")

# Görev Listesi
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

col1, col2 = st.columns([0.8, 0.2])
with col1:
    new_task = st.text_input("", placeholder="Bugün neyi başarmak istiyorsun?", label_visibility="collapsed")
with col2:
    if st.button("Görev Ekle", use_container_width=True):
        if new_task:
            st.session_state.tasks.append({"task": new_task, "done": False})
            st.rerun()

# Görevleri Listeleme
st.subheader("📌 Görevlerin")
for i, task_obj in enumerate(st.session_state.tasks):
    c1, c2, c3 = st.columns([0.1, 0.7, 0.2])
    
    # Tamamlama kontrolü
    if c1.checkbox("", key=f"check_{i}", value=task_obj["done"]):
        task_obj["done"] = True
        st.balloons() # Başarı konfetisi!
        
    # Görev metni (Tamamlandıysa üstü çizili)
    if task_obj["done"]:
        c2.markdown(f"~~{task_obj['task']}~~")
    else:
        c2.write(task_obj["task"])
        
    # Silme butonu
    if c3.button("🗑️", key=f"del_{i}"):
        st.session_state.tasks.pop(i)
        st.rerun()

st.divider()

# Pomodoro Bölümü
st.subheader("⏱️ Odaklanma Zamanlayıcısı")
mins = st.slider("Kaç dakika odaklanacaksın?", 1, 60, 25)

if st.button("🔥 Odaklanmaya Başla", use_container_width=True):
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(mins * 60, 0, -1):
        mm, ss = divmod(i, 60)
        status_text.metric("Kalan Süre", f"{mm:02d}:{ss:02d}")
        
        # İlerleme çubuğunu güncelle
        percent = 100 - (i / (mins * 60) * 100)
        progress_bar.progress(int(percent))
        
        time.sleep(1)
    
    st.success("Tebrikler! Bir seansı daha başarıyla bitirdin. 🎉")
    st.snow() # Kar efekti!