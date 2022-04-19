/**
 * Join room by room id & auth token
 * @param {string} channel
 * @returns {void}
 * @author: Ehsan Ghaffar
 * @version: 1.0.0
 * @since: 2019-01-01
 * @license: MIT
 */

const fetch = require("node-fetch");

let url = "https://www.clubhouseapi.com/api/join_channel";

let token = "YOUR_AUTH_TOKEN";
let roomID = "YOUR_ROOM_ID";

let options = {
  method: "POST",
  headers: {
    "CH-Languages": "en-US",
    "CH-Locale": "en_US",
    Accept: "application/json",
    "Accept-Encoding": "gzip, deflate",
    "CH-AppBuild": "2576",
    "CH-AppVersion": "1.0.0",
    "CH-UserID": "<id>",
    "User-Agent": "clubhouse/490 (iPhone; iOS 14.4; Scale/2.00)",
    Connection: "alive",
    "Content-Type": "application/json; charset=utf-8",
    Authorization: "Token" + token,
  },
  body: `{\n	"channel": "${roomID}"\n}\n`,
};

fetch(url, options)
  .then((res) => res.json())
  .then((json) => console.log(json))
  .catch((err) => console.error("error:" + err));
