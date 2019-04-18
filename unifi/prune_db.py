import logs.mon_log as mlog
import subprocess

def prune():
    f = open("mongo_prune_js.js")
    cmd = "mongo --port 27117"
    try:
        p1 = subprocess.Popen(cmd.split(" "), stdin=f, stdout=subprocess.PIPE)
        outs, errs = p1.communicate()
        mlog.monLog.warning("Pruning mongodb to clean disk space")
        mlog.monLog.warning(str(outs, 'utf-8'))
    except subprocess.CalledProcessError as e:
        mlog.monLog.exception(e, __name__)
