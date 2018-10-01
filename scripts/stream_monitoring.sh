#! /bin/bash
cd $1
# send update notification
python $PWD/streaming/scripts/update_notification.py $PWD/tweets.db "peters@is.tu-darmstadt.de" "Twitter Stream"
# backup database file
sh $PWD/streaming/scripts/db_backup.sh $PWD/tweets.db s3://tep-research-project/backups/
