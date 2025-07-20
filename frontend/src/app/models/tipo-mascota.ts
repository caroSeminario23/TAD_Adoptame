export class TipoMascota {
  id_tipo_mascota : number;
  nombre: string;

  constructor(
    id_tipo_mascota: number,
    nombre: string
  ) {
    this.id_tipo_mascota = id_tipo_mascota;
    this.nombre = nombre;
  }
}
