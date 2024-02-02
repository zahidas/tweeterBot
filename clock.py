#coding:utf-8

# import library
from apscheduler.schedulers.blocking import BlockingScheduler
from tweet import TwitterUtil

# Function to execute
def timed_job(twitter_util):
    twitter_util.post()

if __name__ == "__main__": # t_range: [-t_range, +t_range] seconds
    sc = BlockingScheduler( timezone='Asia/Tokyo' )
    tweet1 = "Sample tweet 1"
    tweet2 = "Sample tweet 2"
    sample1 = TwitterUtil( id="sample1", text=tweet1, post_time="23:10:00", pos_tim_rad=False)
    sample2 = TwitterUtil( id="sample2", text=tweet2, post_time="23:20:00", pos_tim_rad=True, t_range=300)
    Class_list = [sample1, sample2]
    for cla in Class_list:
        pt = cla.post_time
        #sc.add_job( timed_job, 'interval', args=[cla], id=cla.id, minutes=2 )
        if (cla.post_time_random == True):
            sc.add_job( timed_job, 'cron', args=[cla], id=cla.id, \
                        hour=pt.hour, minute=pt.minute, jitter=cla.time_range )
        else:
            sc.add_job( timed_job, 'cron', args=[cla], id=cla.id, hour=pt.hour, minute=pt.minute )
    sc.start()


# .add_job( timed_job, 'interval', args=[cla], id=cla.id, minutes=2 )
# .add_job( timed_job, 'cron', args=[cla], id=cla.id, hour=pt.hour, minute=pt.minute, jitter=cla.t_range )

# reference
# https://qiita.com/nkg/items/0379a0a9c45af58640f5
# https://apscheduler.readthedocs.io/en/stable/userguide.html
# https://nerimplo.hatenablog.com/entry/2019/02/26/184500
# https://www.fixes.pub/program/268636.html
# https://apscheduler.readthedocs.io/en/stable/modules/triggers/interval.html