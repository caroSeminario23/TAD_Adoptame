import {TipoMascota} from './tipo-mascota';
import {Raza} from './raza';

export class Mascota {
  id_mascota : number;
  id_tipo_mascota: number;
  id_raza: number;
  nombre: string;
  foto: string;
  fec_nacimiento: Date;
  sexo: string;
  estatura: number;
  peso: number;
  fec_ingreso: Date;
  adoptado: boolean;
  discapacidad: boolean;
  tipo_mascota: TipoMascota;
  raza: Raza;
  origen: string;
  caracteristicas: { nombre: string, valor: string }[];

  constructor(
    id_mascota : number,
    id_tipo_mascota: number,
    id_raza: number,
    nombre: string,
    foto: string,
    fec_nacimiento: Date,
    sexo: string,
    estatura: number,
    peso: number,
    fec_ingreso: Date,
    adoptado: boolean,
    discapacidad: boolean,
    tipo_mascota: TipoMascota,
    raza: Raza,
    origen: string,
    caracteristicas: { nombre: string, valor: string }[] = []
  ) {
    this.id_mascota = id_mascota;
    this.id_tipo_mascota = id_tipo_mascota;
    this.id_raza = id_raza;
    this.nombre = nombre;
    this.foto = foto;
    this.fec_nacimiento = fec_nacimiento;
    this.sexo = sexo;
    this.estatura = estatura;
    this.peso = peso;
    this.fec_ingreso = fec_ingreso;
    this.adoptado = adoptado;
    this.discapacidad = discapacidad;
    this.tipo_mascota = tipo_mascota;
    this.raza = raza;
    this.origen = origen;
    this.caracteristicas = caracteristicas || [];
  }
}
