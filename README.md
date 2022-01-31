# Awesome Clubhouse

<img src="screenshot.png" alt="clubhouse" width="300" />

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Clubhouse is a new type of social network based on voice—where people around the world come together to talk, listen and learn from each other in real-time.

Feel free to take a look. You might learn new things. They have been designed to provide a quick way to assess your knowledge and to save you time.


---

- [Content](#content)
    - [Official](#official)
    - [Developer Tools](#developer-tools)
    - [Top Clubs](#top-clubs)
        - [Tech](#tech)
        - [Science](#science)
        - [Movie](#movie)
        - [Food & Drink](#food-drink)
        - [Education](#education)
        - [Market](#market)
        - [Fun](#fun)
    - [Code Snippets](#code-snippets)
        - [Python](#python)
        - [NodeJS](#nodejs)
    - [End Points](#end-points)
- [Resources](#resources)
    - [Articles](#aericles)
    - [Newsletters](#newsletters)
    - [Videos](#videos)
    - [Websites](#websites)



<!--start-->

# Content


## Official

* [Official Website](https://clubhouse.com)
* [Official Android App](https://play.google.com/store/apps/details?id=com.clubhouse)
* [Official iOS App](https://itunes.apple.com/us/app/clubhouse/id1209829091)

## Developer Tools

* [Python API](https://github.com/stypr/clubhouse-py) Clubhouse cli API create with Python
* [Clubhouse Desktop](https://github.com/callmearta/clubhouse-desktop) An unofficial Clubhouse desktop client developed with ElectronJS
* [Swagger API](https://github.com/zhuowei/ClubhouseAPI) Web service for Clubhouse API with Swagger
* [Open Clubhouse](https://github.com/ai-eks/OpenClubhouse) A third-part web application based on flask to play Clubhouse audio.
* [HouseClub](https://github.com/grishka/Houseclub) A barebones unofficial Android app for Clubhouse.
* [Clubhouse Flutter](https://github.com/perpetio/clubhouse) Clubhouse clone built on Flutter
* [TypeScript Clubhouse](https://github.com/transitive-bullshit/clubhouse) Clubhouse API client and social graph crawler for TypeScript.
* [hipster-house](https://github.com/zhuowei/hipster.house) An intentionally terrible third-party Clubhouse client for web browsers.
* [AnyHouse](https://github.com/anyRTC-UseCase/anyHouse) 高仿 ClubHouse，语音直播、语聊房、高音质、极速上麦，开源 ClubHouse，实现了Clubhouse的上麦，下麦，邀请，语音音量提示等功能。
* [PHP Clubhouse](https://github.com/fadhiilrachman/clubhouse-api-php) 👋 Clubhouse API library for PHP



## Top Clubs

  * Tech
    * [Tech & Chill](https://www.clubhouse.com/club/techchill)
    * [Startup Club](https://clubhousedb.com/club/45-startup-club)
    * [Tech Talks](https://clubhousedb.com/club/3225-tech-talks)
    * [Github](https://clubhousedb.com/club/735673473-github) Unofficial Github Club
    
  * Programming
    * [Python](https://clubhousedb.com/club/598487268-python) Coding and programming enthusiasts, Feel free to start rooms! Open to all levels! Suggest your friends as members!
    * [Javascript](https://clubhousedb.com/club/1253333235-javascript) JavaScript is the everywhere language; one of the most popular programming language in the world.
    * [Persian Developers Hub](https://clubhousedb.com/club/1630392162-persian-developers-hub) A community of developers who share their knowledge and experience in the field of web development.
    * [Programmers](https://www.clubhouse.com/club/%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%D8%A7%D9%86) 

  * Science
    * [Human Behaviour](https://clubhousedb.com/club/156-human-behaviour) This club is for everyone interested in - neuroscience/ decision-making, health/ wellness, tech/ computer science, marketing/ influence, start-ups/ VC

  * Movie
    * [Movie Club](https://clubhousedb.com/club/105-movie-club) It's like book club but for movies
  
  * Food & Drink
    * [Plant-based Food + Wellness](https://clubhousedb.com/club/307-plant-based-food-wellness) From curious carnivore to fully vegan, all diets are welcome as we cook up healthy ways to get more plants on our plates with talks from the founders, funders and foodies in the nutrition + plant-based space.

  * Education
    * [What Are You Reading?](https://clubhousedb.com/club/764-what-are-you-reading) Let's talk about what we're reading. It can be books, articles, blog posts, magazines, or whatever.
    * [English Language](https://clubhousedb.com/club/290630288-english-language) Network and practice speaking with people from all around the world using the English Language.

  * Market
    * [Bitcoin](https://clubhousedb.com/club/597-bitcoin) A club for open and friendly dialog on bitcoin technology, markets, culture, and ecosystem.
    * [Marketing Club](https://clubhousedb.com/club/131-marketing-club)  A community for all things marketing. 

  * Fun
    * [Beauty and The Geek](https://www.clubhouse.com/club/beauty-and-the-geek) A club for the beauty and the geeks
    * [Comedy Club](https://clubhousedb.com/club/1024-comedy-club) The original and largest comedy community on Clubhouse with your favorite comedians, comedy writers, improv & sketch performers, and basically all things funny!
    * [Hot Developers](https://www.clubhouse.com/club/hot-persiandevelopers)
  
    

## Code Snippets

* Python

<details>
<summary>📃 View code snippets </summary>

  * Payload example

  ```python
  
  payload = "{\r\n \"channel\": \"MwkK3arv\" , \"user_id\": 1928455578  \r\n}"
  
  ````
  
  * Headers examples

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
 </details>


* NodeJS
 
<details>
<summary>📃 View code snippets </summary>

  * Payload example
    
  ```javascript
   
    payload = { 
            "channel": "MwkK3arv",
            "user_id": "1928455578"
            }
  ```

</details>
  

## End Points

Full list of [Clubhouse](https://clubhouse.com) API endpoints.

<details>
<summary>📃 View End-Point list</summary>

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
</details>


# Resources

## Articles

* [Analyzing Clubhouse](https://blog.theori.io/research/korean/analyzing-clubhouse/)

## Newsletters

* [Clubhouse Newsletter](https://www.clubhouse.com/newsletter)

## Videos


## Websites

* [Clubhouse](https://www.clubhouse.com/)
* [Clubhouse Api](https://clubhouseapi.com/)
* [Clubhouse-cli](https://github.com/ehsanghaffarii/clubhouse-cli)


# Contributing

Your contributions are always welcome! Please take a look at the [contribution guidelines](https://github.com/ehsanghaffarii/awesome-clubhouse/blob/main/CONTRIBUTING.md) first.

I will keep some pull requests open if I'm not sure whether those libraries are awesome, you could [vote for them](https://github.com/ehsanghaffarii/awesome-clubhouse) by adding :+1: to them.

- - -

If you have any question about this opinionated list, do not hesitate to contact me [@ehsanghaffar](https://twitter.com/ehsanghaffarii) on Twitter or open an issue on GitHub.