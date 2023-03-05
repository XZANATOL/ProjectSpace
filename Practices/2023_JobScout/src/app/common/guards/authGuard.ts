import { inject } from '@angular/core';
import { Router } from '@angular/router';
import PocketBase from 'pocketbase';

import { environment } from '../../../environments/environment'

export const authGuard = () => {
	let pb = new PocketBase(environment.Db_URL);
	const router = inject(Router);

	let cookie: any = localStorage.getItem("pocketbase_auth")
	if (cookie == null){
		return router.parseUrl("/")
	}

	pb.authStore.loadFromCookie(cookie)
	if (pb.authStore.isValid){
		localStorage.setItem("pocketbase_auth", cookie)
		return true
	}
	localStorage.setItem("pocketbase_auth", "") // Reset cookie
	return router.parseUrl("/")
}