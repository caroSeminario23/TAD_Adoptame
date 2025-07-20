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
  listarCarComplementarias(): Observable<any> {
    return this.http.get<any>(this.urlBackEnd.obtenerUrlBackend() + 'federador_routes/listar_car_complementarias')
    .pipe(map(response => response.data));
  }

  listarCarMascotas(): Observable<any> {
    return this.http.get<any>(this.urlBackEnd.obtenerUrlBackend() + 'federador_routes/listar_car_mascotas')
    .pipe(map(response => response.data));
  }

  listarMascotas(): Observable<any> {
    return this.http.get<any>(this.urlBackEnd.obtenerUrlBackend() + 'federador_routes/listar_mascotas')
    .pipe(map(response => response.data));
  }

  listarRazas(): Observable<any> {
    return this.http.get<any>(this.urlBackEnd.obtenerUrlBackend() + 'federador_routes/listar_razas')
    .pipe(map(response => response.data));
  }

  listarTiposMascotas(): Observable<any> {
    return this.http.get<any>(this.urlBackEnd.obtenerUrlBackend() + 'federador_routes/listar_tipos_mascotas')
    .pipe(map(response => response.data));
  }

  buscarCarComplementaria(CaracteristicaMascota: any): Observable<any> {
    return this.http.post<any>(this.urlBackEnd.obtenerUrlBackend() + 'federador_routes/buscar_caracteristica_complementaria', 
    { id_caracteristica : CaracteristicaMascota.id_caracteristica,
      origen : CaracteristicaMascota.origen,
     })
    .pipe(map(response => response.data));
  }

  buscarCarMascota(Mascota: any, id_caracteristica: any): Observable<any> {
    return this.http.post<any>(this.urlBackEnd.obtenerUrlBackend() + 'federador_routes/buscar_car_mascota', 
    { id_caracteristica : id_caracteristica,
      id_mascota: Mascota.id_mascota,
      origen : Mascota.origen,
     })
    .pipe(map(response => response.data));
  }  

  buscarMascota(Mascota: any): Observable<any> {
    return this.http.post<any>(this.urlBackEnd.obtenerUrlBackend() + 'federador_routes/buscar_mascota', 
    { id_mascota : Mascota.id_mascota,
      origen : Mascota.origen,
     })
    .pipe(map(response => response.data));
  }

  buscarRaza(Mascota: any): Observable<any> {
    return this.http.post<any>(this.urlBackEnd.obtenerUrlBackend() + 'federador_routes/buscar_raza', 
    { id_raza : Mascota.id_raza,
      origen : Mascota.origen,
     })
    .pipe(map(response => response.data));
  }

  buscarTipoMascota(Mascota: any): Observable<any> {
    return this.http.post<any>(this.urlBackEnd.obtenerUrlBackend() + 'federador_routes/buscar_tipo_mascota', 
    { id_tipo_mascota : Mascota.id_tipo_mascota,
      origen : Mascota.origen,
     })
    .pipe(map(response => response.data));
  }

}
