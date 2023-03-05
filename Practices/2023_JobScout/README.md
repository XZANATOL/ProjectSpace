# JobScout

An application organizer platform for better tracking job applications when job hunting.

## Usage

*(In Development)*

* Install [NodeJS](https://nodejs.org/en/)
* Install [PocketBase](pocketbase.io/)
	- Go to `./PocketBase` copy `pb_migrations` folder into the same directory of the downloaded PocketBase executable.
	- Run `pocketbase migrate`.
	- Run `pockerbase serve`.
	- Open PocketBase dashboard and add a user in the `users` collection.
	- Go to `./src/environments/` folder and edit the value of `Db_URL` key in `environment.development.ts` file to the PocketBase host IP address.
* run `npm install`
* run `npm run start`

## Demo Video

https://user-images.githubusercontent.com/64689436/220753053-c7cdaaf4-648d-470a-84c0-22eace365b90.mp4

## Design Document

Angular 15 for the frontend. (Practicing Angular.. some of the taken notes can be found in the [notes.md](./notes.md))

[PocketBase](pocketbase.io/) for the backend, which is a platform written in Go with a builtin database, JWT authentication, SDK, and a Restful API all packed into one single executable.

### Database Design

| Field Name	| Type		    |
| ------------- | ------------- |
| user (non-empty) | Relation -> users collection -> Display: email |
| title (non-empty) | Plain Text |
| job_url | Url |
| created | DataTime |
| updated | DataTime |
| cv | File (5MB max) |
| questions | Plain Text |
| notes | Plain Text |
| stage | Select -> Submitted, Accepted, Rejected -> Max-Select: 1 |

