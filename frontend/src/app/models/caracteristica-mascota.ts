import {Caracteristica} from './caracteristica';
import {Mascota} from './mascota';

export class CaracteristicaMascota {
  id_caracteristica : number;
  id_mascota : number;
  valor : string;
  caracteristica: Caracteristica;
  mascota: Mascota;
  origen: string;

  constructor(
    id_caracteristica: number,
    id_mascota: number,
    valor : string,
    caracteristica: Caracteristica,
    mascota: Mascota,
    origen: string
  ) {
    this.id_caracteristica = id_caracteristica;
    this.id_mascota = id_mascota;
    this.valor = valor;
    this.caracteristica = caracteristica;
    this.mascota = mascota;
    this.origen = origen;
  }
}
