import { Injectable } from '@angular/core';
import {UrlBackEnd} from '../url-back-end';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MascotaService {

  constructor(
    private urlBackEnd: UrlBackEnd,
    private http: HttpClient
  ) {
  }

  list(): Observable<any> {
    return this.http.get<any>(this.urlBackEnd.obtenerUrlBackend() + '/get_mascotas');
  }

  typesList(): Observable<any> {
    return this.http.get<any>(this.urlBackEnd.obtenerUrlBackend() + '/get_mascotas');
  }

  breedList(): Observable<any> {
    return this.http.get<any>(this.urlBackEnd.obtenerUrlBackend() + '/get_mascotas');
  }
}


