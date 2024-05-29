-- youtube videos categories 
select
  vc.category_title,
  av.*
from
  quasar.analytics_videos av
  left join public.video_category vc on av.category_id = vc.id

-- stroer verticals
select distinct scv."Vertical New"
from public.stroer_channel_vertical scv

-- era verticals
select distinct cim.vertical
from public.channel_info_months cim
