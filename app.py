"""AEGIS FLOW 2.0 | demonstrator. No operational customs data or deployed AI model."""
import csv
import hashlib
from pathlib import Path
import numpy as np
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title='AEGIS FLOW 2.0 | Customs Intelligence', page_icon='⚓', layout='wide', initial_sidebar_state='expanded')
ROOT=Path(__file__).resolve().parent
NAVY='#10306b'; GOLD='#e8ac39'; BLUE='#1769d2'; GREEN='#16a085'; RED='#e96977'
st.markdown("""<style>
:root{--aegis:#14377a;--aegisblue:#1769d2;--soft:#f2f7ff}
.stApp{background:#f5f9ff;color:#193454}
[data-testid="stHeader"]{background:rgba(255,255,255,.96);border-bottom:1px solid #e7edf7}
section[data-testid="stSidebar"]{background:#ffffff;border-right:1px solid #dce8f8}
section[data-testid="stSidebar"] *{color:#173b73 !important}
section[data-testid="stSidebar"] [data-testid="stAlert"]{background:#eaf4ff;border:1px solid #d4e8ff}
section[data-testid="stSidebar"] [data-testid="stAlert"] *{color:#244a75 !important}
section[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked){background:#e9f2ff;border-radius:12px}
section[data-testid="stSidebar"] [role="radiogroup"] label{padding:7px 9px}
.block-container{padding-top:1.35rem;padding-bottom:3rem;max-width:1500px}
h1,h2,h3,h4,h5,h6{color:#103775 !important;letter-spacing:-.02em}
p,li,label,small,[data-testid="stMarkdownContainer"]{color:#264665}
[data-testid="stMetric"]{background:#ffffff;padding:19px 21px;border:1px solid #e0eafb;border-radius:18px;box-shadow:0 6px 22px rgba(32,91,165,.07);min-height:125px}
[data-testid="stMetricLabel"] *,[data-testid="stMetricLabel"]{color:#54708e !important}
[data-testid="stMetricValue"] *,[data-testid="stMetricValue"]{color:#123f8a !important;font-weight:800}
[data-testid="stMetricDelta"] *{font-weight:700}
[data-testid="stVerticalBlockBorderWrapper"]{border-radius:18px}
[data-testid="stAlert"]{border-radius:14px}
[data-testid="stSelectbox"] label,[data-testid="stSlider"] label{color:#214c80 !important;font-weight:600}
[data-testid="stDataFrame"]{border-radius:16px;overflow:hidden;border:1px solid #e2eaf5}
[data-testid="stPlotlyChart"]{background:white;border:1px solid #e4edf9;border-radius:18px;padding:6px;box-shadow:0 4px 18px rgba(32,91,165,.05)}
[data-testid="stCode"]{border-radius:15px}
.stButton>button,.stDownloadButton>button,.stLinkButton>a{border-radius:11px;background:#1268d2;color:white;border:0}
.hero{background:linear-gradient(90deg,rgba(12,49,108,.96),rgba(12,74,147,.82) 47%,rgba(12,74,147,.10)),url('data:image/jpeg;base64,PORT_BANNER');background-position:center;background-size:cover;border-radius:22px;padding:42px 34px;min-height:240px;margin-bottom:23px;box-shadow:0 14px 32px rgba(35,89,154,.15)}
.hero h1{color:white !important;font-size:clamp(34px,4vw,54px);margin:4px 0 12px;line-height:1.05}
.hero p,.hero small{color:#e8f3ff !important;font-size:16px;max-width:620px}
.hero .eyebrow{color:#bde2ff !important;font-weight:700;font-size:12px;letter-spacing:.13em}
.hero .chip{display:inline-block;border:1px solid rgba(255,255,255,.4);background:rgba(255,255,255,.16);color:white;border-radius:100px;padding:7px 13px;margin:13px 7px 0 0;font-size:12px}
.section-heading{font-size:22px;font-weight:800;color:#123b79;margin:10px 0 14px}
.provenance{background:#e9f3ff;border:1px solid #d5e7ff;border-radius:13px;padding:13px 16px;color:#225184;font-size:13px;margin:0 0 16px}
@media(max-width:850px){.hero{padding:25px 20px;min-height:200px}.hero h1{font-size:33px}}
</style>""".replace('PORT_BANNER', __import__('base64').b64encode((ROOT/'assets'/'port_banner.jpg').read_bytes()).decode()),unsafe_allow_html=True)

def read_csv(name):
    with open(ROOT/'data'/name,encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
raw=read_csv('apcd_imports_cleaned.csv')
quarters=read_csv('apcd_quarterly_summary.csv')
years=sorted({int(float(r['Year'])) for r in raw})

def money(x):return f'AED {x/1e9:,.2f}B'
def fig_style(fig,height=370):
    fig.update_layout(paper_bgcolor='#ffffff',plot_bgcolor='#ffffff',font_color='#24456c',height=height,margin=dict(l=25,r=25,t=55,b=45),legend=dict(orientation='h',y=-0.27),title_font=dict(size=17,color='#123b79'),xaxis=dict(gridcolor='#eaf0f9',zerolinecolor='#eaf0f9'),yaxis=dict(gridcolor='#eaf0f9',zerolinecolor='#eaf0f9'))
    return fig

st.sidebar.markdown('## ⚓ AEGIS FLOW 2.0')
st.sidebar.caption('SELF-HEALING CUSTOMS INTELLIGENCE')
page=st.sidebar.radio('Explore the platform',['Command Center','Customs Time Machine','Domino Shield','Butterfly Effect','AI Decision Passport','Data & Methodology'])
st.sidebar.divider()
st.sidebar.warning('RESEARCH PROTOTYPE • APCD trade data is real; shipment and delay scenarios are synthetic. No live customs integration.')
st.sidebar.caption('Predict the Disruption · Prevent the Domino Effect · Protect the Flow')

if page=='Command Center':
    st.markdown('''<div class="hero"><div class="eyebrow">WELCOME TO THE FUTURE OF CUSTOMS INTELLIGENCE</div><h1>AEGIS FLOW 2.0</h1><p>Self-Healing Customs Intelligence for Smarter Port Operations</p><span class="chip">◈ Predictive Simulation</span><span class="chip">◈ Domino Shield</span><span class="chip">◈ Explainable Decisions</span></div>''',unsafe_allow_html=True)
else:
    st.caption('⚓ AEGIS FLOW 2.0  /  INTERACTIVE RESEARCH PROTOTYPE')

if page=='Command Center':
    st.markdown('<div class="section-heading">📊 Customs Intelligence Command Center</div>',unsafe_allow_html=True)
    st.markdown('<div class="provenance">✓ OFFICIAL APCD OPEN DATA — Import values and reported weights are historical aggregates. All shipment-level scenarios elsewhere in this demo are synthetic.</div>',unsafe_allow_html=True)
    a,b=st.columns([1,2])
    with a: selected=st.selectbox('Year', ['All years']+years,index=len(years))
    with b: region=st.selectbox('Trade region',['All regions']+sorted({r['Region EN'] for r in raw}))
    rows=[r for r in raw if (selected=='All years' or int(float(r['Year']))==selected) and (region=='All regions' or r['Region EN']==region)]
    value=sum(float(r['Value in (AED)']) for r in rows)
    weight=sum(float(r['Weight (Ton)']) for r in rows)
    c1,c2,c3,c4=st.columns(4)
    c1.metric('Import value',money(value));c2.metric('Reported weight',f'{weight/1e6:,.2f}M t');c3.metric('Records',len(rows));c4.metric('Regions',len({r['Region EN'] for r in rows}))
    q={}
    for r in rows:
        key=(int(float(r['Year'])),int(float(r['Quarter'])))
        q[key]=q.get(key,0)+float(r['Value in (AED)'])
    keys=sorted(q)
    fig=go.Figure(go.Scatter(x=[f'{y} Q{k}' for y,k in keys],y=[q[x]/1e9 for x in keys],mode='lines+markers',line=dict(color=BLUE,width=4),fill='tozeroy',fillcolor='rgba(23,105,210,0.11)',name='Import value'))
    fig.update_layout(title='Import value by quarter (AED billions)',yaxis_title='AED billions')
    st.plotly_chart(fig_style(fig),use_container_width=True)
    grouped={}
    for r in rows:grouped[r['Region EN']]=grouped.get(r['Region EN'],0)+float(r['Value in (AED)'])
    fig2=go.Figure(go.Bar(x=list(grouped),y=[v/1e9 for v in grouped.values()],marker_color=BLUE))
    fig2.update_layout(title='Import value by trade region',yaxis_title='AED billions')
    st.plotly_chart(fig_style(fig2,330),use_container_width=True)
    st.caption('Source: APCD Open Data — Import Volume Grouped by Region. Values are aggregated historical trade figures, not shipment counts or observed clearance delays.')

# Deterministic scenario model: explicitly NOT an ML prediction model.
def simulate(n,inspect_count,docs_delay,priority,seed=17):
    rng=np.random.default_rng(seed)
    arrivals=np.sort(rng.uniform(0,150,n))
    service=rng.uniform(12,27,n)
    doc_times=rng.uniform(7,20,n)+docs_delay*rng.binomial(1,.32,n)
    high=rng.random(n)<.23
    ids=[f'SHP-{i+1:03d}' for i in range(n)]
    # A single document check queue, followed by a shared inspection pool.
    doc_free=0.; ready=[]
    for i in range(n):
        start=max(arrivals[i],doc_free);doc_free=start+doc_times[i]
        ready.append((doc_free,i))
    if priority:ready.sort(key=lambda x:(x[0]//20,not high[x[1]],x[0]))
    else:ready.sort()
    inspect_free=[0.]*inspect_count;finished=np.zeros(n)
    for r,i in ready:
        lane=int(np.argmin(inspect_free));start=max(r,inspect_free[lane]);finished[i]=start+service[i];inspect_free[lane]=finished[i]
    elapsed=finished-arrivals
    return {'ids':ids,'arrivals':arrivals,'finish':finished,'elapsed':elapsed,'high':high,'total':float(elapsed.sum()),'avg':float(elapsed.mean()),'late':int((elapsed>80).sum()),'finish_max':float(finished.max())}

if page=='Customs Time Machine':
    st.subheader('⏳ Customs Time Machine')
    st.write('Explore alternative futures before deciding. **All shipment events and processing times below are synthetic.**')
    a,b,c=st.columns(3)
    n=a.slider('Simulated shipments',30,180,90,10)
    lanes=b.slider('Inspection stations',1,8,3)
    delay=c.slider('Documentation disruption (minutes)',0,90,40,5)
    priority=st.toggle('Test risk-aware prioritization (simulation only)',value=False)
    baseline=simulate(n,lanes,delay,False)
    alternative=simulate(n,lanes+1,delay,priority)
    st.caption('Intervention A: add one hypothetical inspection station; optionally enable risk-aware prioritization. Fixed seed permits fair comparison.')
    k1,k2,k3=st.columns(3)
    k1.metric('Baseline mean clearance',f"{baseline['avg']:.1f} min")
    k2.metric('Alternative mean clearance',f"{alternative['avg']:.1f} min",delta=f"{alternative['avg']-baseline['avg']:.1f} min",delta_color='inverse')
    k3.metric('Change in total wait+processing',f"{baseline['total']-alternative['total']:,.0f} min")
    fig=go.Figure()
    fig.add_trace(go.Histogram(x=baseline['elapsed'],name='Baseline',marker_color=RED,opacity=.72))
    fig.add_trace(go.Histogram(x=alternative['elapsed'],name='Alternative',marker_color=GREEN,opacity=.72))
    fig.update_layout(title='Simulated shipment clearance duration',xaxis_title='Minutes',yaxis_title='Shipments',barmode='overlay')
    st.plotly_chart(fig_style(fig),use_container_width=True)
    st.info('Simulation result, not a real-world performance forecast. The intervention adds hypothetical capacity and does not waive any customs control.')

if page=='Domino Shield':
    st.subheader('🛡️ AEGIS Domino Shield')
    st.write('Trace potential knock-on delays when shipments share processing resources.')
    n=st.slider('Shipments in dependency graph',10,35,20)
    origin=st.selectbox('Disrupted shipment',[f'SHP-{i+1:03d}' for i in range(n)])
    severity=st.slider('Initial disruption (minutes)',10,100,45,5)
    rng=np.random.default_rng(2026)
    # Directed acyclic graph with a limited number of successors per node.
    edges=[]
    for i in range(n):
        for j in range(i+1,min(n,i+4)):
            if rng.random()<.42:edges.append((i,j,float(rng.uniform(.25,.65))))
    origin_i=int(origin.split('-')[1])-1
    effects=np.zeros(n);effects[origin_i]=severity
    for i in range(origin_i,n):
        for u,v,w in edges:
            if u==i:effects[v]=max(effects[v],effects[u]*w)
    affected=[i for i in range(n) if effects[i]>=1 and i!=origin_i]
    c1,c2,c3=st.columns(3)
    c1.metric('Disrupted shipment',origin);c2.metric('Potential downstream impacts',len(affected));c3.metric('Sum of simulated knock-on minutes',f'{sum(effects[affected]):.1f}')
    xs=[i%7 for i in range(n)];ys=[-(i//7) for i in range(n)]
    fig=go.Figure()
    for u,v,w in edges:
        fig.add_trace(go.Scatter(x=[xs[u],xs[v]],y=[ys[u],ys[v]],mode='lines',line=dict(color='#bfd0e8',width=1.5),hoverinfo='skip',showlegend=False))
    colors=[GOLD if i==origin_i else RED if effects[i]>=1 else BLUE for i in range(n)]
    fig.add_trace(go.Scatter(x=xs,y=ys,mode='markers+text',text=[f'{i+1}' for i in range(n)],textposition='middle center',textfont=dict(color='white',size=10),marker=dict(color=colors,size=32,line=dict(color='#ffffff',width=1.5)),customdata=[[f'SHP-{i+1:03d}',round(effects[i],1)] for i in range(n)],hovertemplate='%{customdata[0]}<br>Propagated delay: %{customdata[1]} min<extra></extra>',showlegend=False))
    fig.update_xaxes(visible=False);fig.update_yaxes(visible=False)
    st.plotly_chart(fig_style(fig,440),use_container_width=True)
    st.caption('Graph connections and propagation weights are generated for demonstration, not inferred from APCD shipment records. Gold = selected disruption; red = downstream impact.')

if page=='Butterfly Effect':
    st.subheader('🦋 Customs Butterfly Effect')
    st.write('Compare small operational interventions by their **simulated system-wide impact**.')
    n=st.slider('Number of synthetic shipments',40,160,90,10)
    baseline=simulate(n,3,45,False)
    scenarios=[('Baseline',3,45,False,0),('Add one inspection station',4,45,False,1),('Resolve documentation issue early',3,15,False,1),('Combine both interventions',4,15,False,2),('Prioritize risk-tagged cases',3,45,True,1)]
    results=[]
    for name,lanes,doc,priority,cost in scenarios:
        r=simulate(n,lanes,doc,priority)
        results.append({'Intervention':name,'Mean duration (min)':round(r['avg'],1),'Total time saved (min)':round(baseline['total']-r['total'],1),'Late shipments (>80 min)':r['late'],'Effort index (illustrative)':cost})
    st.dataframe(results,use_container_width=True,hide_index=True)
    best=max(results[1:],key=lambda x:x['Total time saved (min)'])
    if best['Total time saved (min)']>0:
        st.success(f"Best simulated total-time improvement: {best['Intervention']} — {best['Total time saved (min)']:,.0f} shipment-minutes saved vs baseline.")
    else:
        st.info('No simulated intervention provides a positive total-time benefit in this scenario. Maintain baseline pending further analysis.')
    fig=go.Figure(go.Bar(x=[r['Intervention'] for r in results],y=[r['Total time saved (min)'] for r in results],marker_color=[GOLD if r==best else BLUE for r in results]))
    fig.update_layout(title='Simulated reduction in cumulative shipment duration',yaxis_title='Shipment-minutes saved')
    st.plotly_chart(fig_style(fig),use_container_width=True)
    st.caption('Effort index is illustrative, not a real cost estimate. Simulation does not consider all staffing, security, or legal constraints; decisions require authorized review.')

if page=='AI Decision Passport':
    st.subheader('🪪 AI Decision Passport')
    st.write('An auditable record of **why** an intervention was proposed, what was simulated, and who must approve it.')
    n=st.slider('Synthetic shipment load',40,140,80,10)
    baseline=simulate(n,3,45,False); alt=simulate(n,4,45,False)
    evidence=f'{n}|3|4|45|{baseline["total"]:.2f}|{alt["total"]:.2f}'
    passport='DEMO-'+hashlib.sha256(evidence.encode()).hexdigest()[:12].upper()
    st.markdown(f'### Passport `{passport}`')
    c1,c2=st.columns(2)
    with c1:
        st.markdown('**Proposed intervention**')
        st.write('Temporarily assign one additional inspection station in the simulated scenario.' if baseline['total']-alt['total']>0.5 else 'No capacity intervention recommended: the extra station produces no meaningful simulated improvement.')
        st.markdown('**Evidence**')
        st.write(f"Synthetic load: {n} shipments; baseline mean {baseline['avg']:.1f} min; alternative mean {alt['avg']:.1f} min.")
        st.markdown('**Expected simulated benefit**')
        st.write(f"{baseline['total']-alt['total']:,.0f} cumulative shipment-minutes saved." if baseline['total']-alt['total']>0.5 else 'No demonstrated time saving in this synthetic scenario; further analysis is required.')
    with c2:
        st.markdown('**Uncertainty and limitations**')
        st.write('Hypothetical arrival and service-time distributions; no calibrated APCD clearance model. No confidence interval or validated operational effect.')
        st.markdown('**Policy safeguards**')
        st.write('No bypass of inspection, risk controls, payment, documentation, or customs approvals.')
        st.markdown('**Authorization**')
        status=st.radio('Human review status',['Pending authorized review','Approved for simulation only','Rejected for simulation'],horizontal=False)
    st.code(f'Passport ID: {passport}\nData classification: SYNTHETIC\nModel: Rule-based discrete-event simulation\nDecision: {status}\nLive system action: NONE',language='text')
    st.caption('Review status is temporary in this demo; no persistent audit log or identity verification is implemented.')

if page=='Data & Methodology':
    st.subheader('📚 Data Provenance & Methodology')
    st.markdown('**Official APCD open data**')
    st.write('Import Volume Grouped by Region, historical quarterly aggregates. Fields: Year, Quarter, Region, Value in AED, Weight in tons. 223 imported records, with standardized region names and review flags for unusual weight values.')
    st.markdown('**Synthetic simulation**')
    st.write('Shipment arrivals, document processing, inspection service times, risk tags, queue resources and disruption propagation are generated locally. The Time Machine is a deterministic two-stage queue simulation, not a trained AI forecasting model.')
    st.markdown('**What is NOT yet implemented**')
    st.write('A validated machine-learning delay predictor, live APCD integration, operational policy engine, persistent audit log, secure authentication, and deployment to customs infrastructure. These are planned future phases.')
    st.markdown('**Data quality caveat**')
    st.write('Reported weights include values flagged for review. They are preserved as published and should not be interpreted as verified without source confirmation.')
    st.link_button('Official APCD dataset page','https://data.ajman.ae/explore/dataset/import-volume-grouped-by-region/api/?flg=en-gb')
    st.download_button('Download cleaned official data',data=(ROOT/'data'/'apcd_imports_cleaned.csv').read_bytes(),file_name='apcd_imports_cleaned.csv',mime='text/csv')
