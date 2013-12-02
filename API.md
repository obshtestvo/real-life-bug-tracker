# API

## Endpoint

### `GET /signals/`

```
?lat=...&lng=...&radius=...&type=...&status =...&user=...&nonstrict=[<parameter names>]&limit=...
```
#### Required parameters

 - lat
 - lng
 - radius
 - limit

Listing all signals from certain location around certain radius.
Could be filtered by category.

`nonstrict` is list of strings. "Non strict" marks parameters that
we want to filter the signals by but we also want all other non-matching
results listed afterwards.

### `POST /signals/`

Multipart body will include:

 - `type`
 - `lng`
 - `lat`
 - `status` - can  only be `“new”` or `“duplicate”`
 - `address` (because we already reverse geocoded the location to reduce requests from geocoding every time)
 - `city`
 - `country` (... empty defaults to `"BG"`?)
 - `short description` (optional)
 - `photo`
 - `details` (text)

Session contains the logged in user.

Three new events are also added in the “dates” property:

 -  `{event: “added”, date: “2013-11-14”}`
 -  `{event: “last_updated”, date: “2013-11-14”}`
 -  `{event: “last_confirmed”, date: “2013-11-14”}`

Where `2013-11-14` is the current date

### `GET /signal/id`
Return all the info for the signal

### `PUT /signal/id`
Scenarios:

#### Add duplicate
Params:

 - `ids` -> list of ids of signals to be added in

Also updates the `“last_updated”` event in the `“dates”` property
`{event: “last_updated”, date: “2013-11-14”} `

####Mark as solved
Multipart body including

 - photo

Adds new event in the `“dates”` property `{event: “solved”, date: “2013-11-14”}`
and the status is changed to `“solved”`. Where `2013-11-14` is the current date

#### Mark as invalid (admin only - most likely to be manual?)
No parameters

Simply switches state to “invalid” and adds new event in the `“dates”`
property `{event: “invalid”, date: “2013-11-14”}`. Where `2013-11-14` is the current date

#### Confirm signal is still existing
No parameters

Updates the `“last_confirmed”` event in the `“dates”` property `{event: “last_confirmed”, date: “2013-11-14”}`.
Where `2013-11-14` is the current date

#### `GET /signal/types`
No params
Get all signal types/categories
