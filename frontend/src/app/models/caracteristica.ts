export class Caracteristica {
  id_caracteristica : number;
  nombre: string;
  unidad_medida: string;

  constructor(
    id_caracteristica: number,
    nombre: string,
    unidad_medida: string
  ) {
    this.id_caracteristica = id_caracteristica;
    this.nombre = nombre;
    this.unidad_medida = unidad_medida;
  }
}
