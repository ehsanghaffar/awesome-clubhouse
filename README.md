# Awesome Clubhouse

<img src="screenshot.png" alt="clubhouse" width="300" />

Clubhouse is a new type of social network based on voice—where people around the world come together to talk, listen and learn from each other in real-time.

## Important To Known

FOR REFERENCE AND EDUCATION PURPOSES ONLY. THIS DOES NOT COME WITH ANY KINDS OF WARRANTY.

## contents


- [Awesome Clubhouse](#awesome-clubhouse)
- [Contents](#contents)
- [Developer Tools](#developer-tools)
- [Code Snippets](#code-snippets)
  - [Python](#python)
  - [NodeJS](#nodejs)
- [End Points](#end-points)
- [Reference](#reference)
- [License](#license)



<!--start-->

#### Developer Tools

- [Official Website](https://www.clubhouse.com/)
- [Python API](https://github.com/stypr/clubhouse-py) Clubhouse cli API create with Python
- [Clubhouse Desktop](https://github.com/callmearta/clubhouse-desktop) An unofficial Clubhouse desktop client developed with ElectronJS
- [Swagger API](https://github.com/zhuowei/ClubhouseAPI) Web service for Clubhouse API with Swagger


#### Code Snippets

   ##### Python

   - Payload example


  ```python
  
  payload = "{\r\n \"channel\": \"MwkK3arv\" , \"user_id\": 1928455578  \r\n}"
  
  ````
  
   - Headers examples

  ```python
  
  headers = {
        'CH-Languages': 'en-US',
        'CH-Locale': 'en_US',
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate',
        'CH-AppBuild': '490',
        'CH-AppVersion': '1.0.0',
        'CH-UserID': '990405533',
        'User-Agent': 'clubhouse/490 (iPhone; iOS 14.4; Scale/2.00)',
        'Connection': 'close',
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Token '+token[i]
        }
        
  ```
 
   ##### NodeJS
  
   - Payload example
   
   
  ```javascript
   
    payload = { 
            "channel": "MwkK3arv",
            "user_id": "1928455578"
            }
  ```
  


#### End Points

A minimal list of [Clubhouse](https://clubhouse.com) API

```bash
get_release_notes
get_all_topics
get_topic
get_clubs_for_topic
get_users_for_topic
update_name
update_displayname
update_bio
update_username
update_twitter_username
update_skintone
add_user_topic
remove_user_topic
update_notifications
add_email
get_settings
update_instagram_username
report_incident
get_followers
get_following
get_mutual_follows
get_suggested_follows_friends_only
get_suggested_follows_all
get_suggested_follows_similar
ignore_suggested_follow
follow
follow_multiple
unfollow
update_follow_notifications
block
unblock
get_profile
get_channel
get_channels
get_suggested_speakers
create_channel
join_channel
leave_channel
active_ping
end_channel
invite_speaker
uninvite_speaker
mute_speaker
make_moderator
accept_speaker_invite
reject_speaker_invite
invite_to_existing_channel
audience_reply
make_channel_public
make_channel_social
block_from_channel
get_welcome_channel
reject_welcome_channel
change_handraise_settings
get_create_channel_targets
update_channel_flags
hide_channel
get_notifications
get_actionable_notifications
ignore_actionable_notification
me
get_online_friends
search_users
search_clubs
check_for_update
get_suggested_invites
invite_to_app
invite_from_waitlist
invite_to_new_channel
accept_new_channel_invite
reject_new_channel_invite
cancel_new_channel_invite
add_club_admin
add_club_member
get_club
get_club_members
get_suggested_club_invites
remove_club_admin
remove_club_member
accept_club_member_invite
follow_club
unfollow_club
get_club_nominations
approve_club_nomination
reject_club_nomination
get_clubs
update_is_follow_allowed
update_is_membership_private
update_is_community
update_club_description
update_club_rules
update_club_topics
add_club_topic
remove_club_topic
get_events
get_events_for_user
get_events_to_start
delete_event
create_event
edit_event
get_event 

```

#### Reference

[Clubhouse-cli](https://github.com/ehsanghaffarii/clubhouse-cli)


# LICENSE

This repository is distributed with GNU General Public License v2.0.
