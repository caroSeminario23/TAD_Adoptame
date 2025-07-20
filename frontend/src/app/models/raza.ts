export class Raza {
  id_raza : number;
  nombre: string;
  origen: string;

  constructor(
    id_raza: number,
    nombre: string,
    origen: string
  ) {
    this.id_raza = id_raza;
    this.nombre = nombre;
    this.origen = origen;
  }
}
