

/**
 * Join channel nodejs
 * @param {string} channel
 * @returns {void}
 * @author: Ehsan Ghaffar
 */

 "use strict";
 var __importDefault = (this && this.__importDefault) || function (mod) {
     return (mod && mod.__esModule) ? mod : { "default": mod };
 };
 Object.defineProperty(exports, "__esModule", { value: true });
 exports.joinChannel = void 0;
 const express_1 = __importDefault(require("express"));
 const dotenv_1 = __importDefault(require("dotenv"));
 const node_fetch_1 = __importDefault(require("node-fetch"));
 const f = node_fetch_1.default;
 dotenv_1.default.config();
 const app = (0, express_1.default)();
 const port = parseInt(process.env.PORT || '3000');
 const apiUrl = process.env.API_URL || '';
 const joinPrefix = '/join_channel';
 const token = process.env.TOKEN || '';
 let options = {
     method: 'POST',
     headers: {
         'CH-Languages': 'en-US',
         'CH-Locale': 'en_US',
         Accept: 'application/json',
         'Accept-Encoding': 'gzip, deflate',
         'CH-AppBuild': '2576',
         'CH-AppVersion': '1.0.0',
         'CH-UserID': '<id>',
         'User-Agent': 'clubhouse/490 (iPhone; iOS 14.4; Scale/2.00)',
         Connection: 'alive',
         'Content-Type': 'application/json; charset=utf-8',
         Authorization: 'Token ' + token
     },
     body: ``
 };
 const joinChannel = (channelId) => {
     options.body = `{\n    "channel": "${channelId}"\n}\n\n`;
     (0, node_fetch_1.default)(apiUrl + joinPrefix, options)
         .then(res => res.json())
         .then(json => console.log(json))
         .catch(err => console.log(err));
 };
 exports.joinChannel = joinChannel;
 