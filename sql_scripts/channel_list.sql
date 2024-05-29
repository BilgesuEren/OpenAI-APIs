with channel_list as (
select
    av.video_title,
    av.channel_id,
    av.published_at,
    av.description,
    cim.vertical,
    RANK() OVER (PARTITION BY av.channel_id ORDER BY av.published_at DESC) AS ranking
from quasar.analytics_videos av
join public.channel_vertical cim on av.channel_id = cim.channel_id
where av.channel_id IN (
            'UC9YTp5M6yYgSd6t0SeL2GQw', --gaming --
            'UCvWQOze3mZUVHgHUyCe4s-Q', --tech --
            'UC4cJPXuqa-qGcDZ1sVpWAmw', --education and science --
            'UCCugZuuJpIe12kFIxhFQLxQ', --entertainment --
            'UCzwi1kwlNyJhhLVrHXmvVqA', --lifestyle hobby --
            'UC1bXG2l9YmiyzlaXI0i0pqw', --kids content --
            'UCOGhBBuD_FPCdS4OFew7DwA', --news politics --
            'UC0m0VPPo84UHJ4m7rGl7RwQ', --auto vehicles --
            'UCdTkML-Lu3Ka74D3fiM0jeg', --foods drinks
            'UCiaZSRydY8beFPD886fS0rw' --health fitness --
        )
  and EXTRACT (epoch FROM av.duration:: interval) >= 61
)
select * from channel_list
where ranking < 10