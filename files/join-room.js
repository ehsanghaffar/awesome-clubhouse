/**
 * Join room by room id & auth token
 * @param {string} channel
 * @returns {void}
 * @author: Ehsan Ghaffar
 * @version: 1.0.0
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
