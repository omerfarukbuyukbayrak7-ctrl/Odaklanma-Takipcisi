import streamlit as st
import time
import random

# Sayfa Ayarları
st.set_page_config(page_title="DeepWork Pro", page_icon="🚀", layout="centered")

# Motivasyon Sözleri Havuzu
sozler = [
    "“Başlamak için mükemmel olmana gerek yok, ama mükemmel olmak için başlamana gerek var.”",
    "“Zorluklar, başarıyı daha değerli kılan engellerdir.”",
    "“Bugün yaptıkların, yarınki seni inşa eder.”",
    "“Pes etmeyi düşündüğünde, neden başladığını hatırla.”",
    "“Küçük adımlar, büyük mesafeler katetmeni sağlar.”",
    "“Zekâna değil, çalışma azmine güven.”"
]

# Yan Menü (Sidebar)
with st.sidebar:
    st.title("⚙️ Ayarlar")
    st.write(f"Hoş geldin, **Ömer Faruk**")
    st.divider()
    st.subheader("💡 Günün Motivasyonu")
    st.info(random.choice(sozler)) # Rastgele bir söz seçer
    st.divider()
    st.write("📌 *Tüyo: Odaklanırken telefonunu başka bir odaya bırak!*")

# Ana Başlık
st.title("🚀 DeepWork Odaklanma Takipçisi")
st.markdown("---")

# Görev Listesi Bölümü
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
if not st.session_state.tasks:
    st.write("*Henüz bir görev eklemedin. Hadi bir tane yaz!*")

for i, task_obj in enumerate(st.session_state.tasks):
    c1, c2, c3 = st.columns([0.1, 0.7, 0.2])
    
    if c1.checkbox("", key=f"check_{i}", value=task_obj["done"]):
        if not task_obj["done"]: # Sadece ilk kez işaretlendiğinde balon patlat
            st.balloons()
        task_obj["done"] = True
        
    if task_obj["done"]:
        c2.markdown(f"~~{task_obj['task']}~~")
    else:
        c2.write(task_obj["task"])
        
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
    
    for i in range(mins * 60, -1, -1):
        mm, ss = divmod(i, 60)
        status_text.metric("Kalan Süre", f"{mm:02d}:{ss:02d}")
        
        percent = 100 - (i / (mins * 60) * 100)
        progress_bar.progress(int(percent))
        
        time.sleep(1)
    
    st.success("Tebrikler! Bir seansı daha başarıyla bitirdin. 🎉")
    st.snow()
    # Titreşim ve Bildirim için JavaScript Kodu
    st.components.v1.html(
        """
        <script>
        // Telefonu 3 saniye (3000 ms) titretir
        if (window.navigator && window.navigator.vibrate) {
            window.navigator.vibrate(3000);
        } else {
            console.log("Titreşim bu cihazda desteklenmiyor.");
        }
        </script>
        """,
        height=0,
    )
