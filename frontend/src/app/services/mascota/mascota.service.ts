import { Injectable } from '@angular/core';
import { UrlBackEnd } from '../url-back-end';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class MascotaService {

  constructor(
    private urlBackEnd: UrlBackEnd,
    private http: HttpClient
  ) {
  }
  
  // LISTAR MASCOTAS
  list(): Observable<any> {
    return this.http.get<any>(this.urlBackEnd.obtenerUrlBackend() + 'federador_routes/listar_mascotas')
    .pipe(map(response => response.data));
  }

  buscarTipo(mascota: any): Observable<any> {
    return this.http.post<any>(this.urlBackEnd.obtenerUrlBackend() + 'federador_routes/buscar_tipo_mascota', { id_tipo_mascota: mascota.id_tipo_mascota })
    .pipe(map(response => response.data));
  }

  listarTipos(): Observable<any> {
    return this.http.get<any>(this.urlBackEnd.obtenerUrlBackend() + 'federador_routes/listar_tipos_mascotas')
    .pipe(map(response => response.data));
  }

  listarRazas(): Observable<any> {
    return this.http.get<any>(this.urlBackEnd.obtenerUrlBackend() + 'federador_routes/listar_razas')
    .pipe(map(response => response.data));
  }

  typesList(): Observable<any> {
    return this.http.get<any>(this.urlBackEnd.obtenerUrlBackend() + '/get_mascotas');
  }

  breedList(): Observable<any> {
    return this.http.get<any>(this.urlBackEnd.obtenerUrlBackend() + '/get_mascotas');
  }
}


