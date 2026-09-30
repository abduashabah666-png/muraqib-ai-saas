import streamlit as st
import time

# إعدادات الصفحة البرمجية للواجهة
st.set_page_config(page_title="Binance AI Risk Agent", page_icon="🚨", layout="centered")

st.title("🚨 Binance AI Behavioral Risk Agent")
st.subheader("العقل المدبر لتقييم الخطر النفسي للمتداول في الوقت الفعلي")
st.write("---")

# قسم المدخلات (لوحة تحكم محاكاة صفقات المتداول)
st.sidebar.header("🎛️ لوحة محاكاة الصفقات")
trader_name = st.sidebar.text_input("اسم المتداول المقترح:", "أحمد")
normal_size = st.sidebar.number_input("متوسط حجم صفقاته المعتاد ($):", value=500, step=50)

st.sidebar.subheader("بيانات الصفقة الحالية:")
last_status = st.sidebar.selectbox("نتيجة آخر صفقة للمتداول:", ["LOSS (خسارة)", "WIN (ربح)"])
seconds_since_last = st.sidebar.slider("الوقت المرتد بعد الخسارة (بالثواني):", min_value=5, max_value=600, value=15)
current_size = st.sidebar.number_input("حجم الصفقة الجديدة التي يطلب فتحها الآن ($):", value=2500, step=100)

# محرك الذكاء الاصطناعي لحساب الخطر النفسي
if st.sidebar.button("⚡ تحليل السلوك واتخاذ القرار فورا"):
    st.write(f"### 🔍 تحليل سلوك المتداول المالي والنفسي الحسابي لـ: **{trader_name}**")
    
    with st.spinner('جاري معالجة الانحراف السلوكي عبر محرك الذكاء الاصطناعي...'):
        time.sleep(1) # محاكاة جزء من الثانية لمعالجة البيانات
    
    if "WIN" in last_status:
        risk_score = 0
        action = "✅ وضع آمن: تمرير الصفقة بشكل طبيعي. المتداول في حالة مستقرة بعد الربح."
        st.success(action)
        st.metric(label="مؤشر الخطر النفسي المتوقع", value=f"{risk_score}%")
    else:
        # حساب الانحرافات
        time_deviation = 3600 / max(seconds_since_last, 1)
        size_deviation = current_size / normal_size
        
        # معادلة قياس الخطر النفسي (0 - 100)
        risk_score = int(min((min(time_deviation, 5) * 10) + (min(size_deviation, 5) * 10), 100))
        
        # عرض النتائج التفاعلية بناء على مؤشر الخطر بالكامل
        st.metric(label="⚠️ مؤشر الخطر النفسي المتوقع", value=f"{risk_score}%", delta=f"+{risk_score}% انحراف عاطفي")
        
        if risk_score >= 75:
            st.error(f"🚨🚨 **إنذار أحمر لبينانس:** تم رصد حالة تداول انتقامي حاد وعاطفي (Revenge Trading)! المتداول ضاعف مبلغه بمقدار {size_deviation:.1f} مرات ودخل بعد {seconds_since_last} ثوانٍ فقط من الخسارة.")
            st.warning("🛠️ **الإجراء التلقائي المتخذ خلف الكواليس:** تفعيل وضع التهدئة وإيقاف حساب المتداول مؤقتاً لحمايته ماليًا.")
        elif risk_score >= 45:
            st.warning(f"⚠️ **تحذير أصفر:** المتداول يتصرف بعاطفية وتسرع نسبي. الإجراء: إرسال نافذة نصية فورية للتهدئة والمواساة.")
        else:
            st.success("✅ **وضع مستقر:** تمرير الصفقة بشكل طبيعي بالرغم من الخسارة السابقة، الانحراف مقبول ضمن إدارة المخاطر.")
