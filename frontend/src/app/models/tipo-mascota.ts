export class TipoMascota {
  id_tipo_mascota : number;
  nombre: string;
  origen: string;

  constructor(
    id_tipo_mascota: number,
    nombre: string,
    origen: string
  ) {
    this.id_tipo_mascota = id_tipo_mascota;
    this.nombre = nombre;
    this.origen = origen;
  }
}
