import {ChangeDetectorRef, Component, OnInit} from '@angular/core';
import {Mascota} from '../../models/mascota';
import {TipoMascota} from '../../models/tipo-mascota';
import {Raza} from '../../models/raza';
import {MascotaService} from '../../services/mascota/mascota.service';
import { Caracteristica } from '../../models/caracteristica';

declare var window: any;

@Component({
  selector: 'app-mascota',
  standalone: false,
  templateUrl: './mascota.component.html',
  styleUrl: './mascota.component.css'
})
export class MascotaComponent implements OnInit {
  Math = Math;
  mascota: Mascota = new Mascota(0, 0, 0, '', '', new Date(), '', 0, 0, new Date(), false, false,
    new TipoMascota(0, '', ''),
    new Raza(0, '', ''), '');
  mascotas: Mascota[] = [];
  tipos: TipoMascota[] = [];
  razas: Raza[] = [];
  modal: any;

  tipoSeleccionado: number = 0;
  razaSeleccionada: number = 0;
  sexoSeleccionado: string = ''; // '', 'M', 'F'
  discapacidadSeleccionada: number = -1; // -1: todos, 1: sí, 0: no

  currentPage: number = 1;
  itemsPerPage: number = 10; // Número de elementos por página

  constructor(
    private mascotaService: MascotaService,
    private cdRef: ChangeDetectorRef
  ) {
  }

  ngOnInit(): void {
    this.modal = new window.bootstrap.Modal(document.getElementById('Modal'));
    this.listaMascotas();
    this.listaTipoMascotas();
    this.listaRazas();
  }

  listaMascotas(){
    this.tipoSeleccionado = 0;
    this.razaSeleccionada = 0;
    this.sexoSeleccionado = '';
    this.discapacidadSeleccionada = -1;

    this.mascotaService.listarMascotas().subscribe(
      data => {
        this.mascotas = data;
        //this.asignarNombresTipos(); 
        //this.asignarNombresRazas(); 
      },
      error => console.error("Error al obtener la lista de mascotas:", error)
    );
      
  }

  listaTipoMascotas(){
    this.mascotaService.listarTiposMascotas().subscribe(
      data => {
        this.tipos = data;
        //this.asignarNombresTipos();
      }
    );
  }

  listaRazas(){
    this.mascotaService.listarRazas().subscribe(
      data => {
        this.razas = data;
        //this.asignarNombresRazas();
      }
    );
  }

  /*filtrarMascotasPorRazas(idRaza: number) {
    this.mascotas = [];
    this.mascotaService.listarMascotas().subscribe(data => {
      this.mascotas = data.filter((m: Mascota) => m.id_raza === +idRaza);
    });
  }

  filtrarMascotasPorTipo(idTipo: number) {
    this.mascotas = [];
    this.mascotaService.listarMascotas().subscribe(data => {
      this.mascotas = data.filter((m: Mascota) => m.id_tipo_mascota === +idTipo);
    });
  }*/

  aplicarFiltro() {
    this.mascotaService.listarMascotas().subscribe(data => {
      this.mascotas = data.filter((m: Mascota) =>
        (this.tipoSeleccionado==0 || m?.id_tipo_mascota === +this.tipoSeleccionado) &&
        (this.razaSeleccionada==0 || m?.id_raza === +this.razaSeleccionada) &&
        (!this.sexoSeleccionado || m?.sexo === this.sexoSeleccionado) &&
        (this.discapacidadSeleccionada === -1 || Number(m?.discapacidad) === this.discapacidadSeleccionada)
      );
    });
  }

    
  /*asignarNombresTipos() {
    this.mascotas.forEach(mascota => {
      const tipo = this.tipos.find((t => t.id_tipo_mascota === mascota.id_tipo_mascota));
      if (tipo) {
        mascota.tipo_mascota = tipo;
        console.log(`Tipo asignado: ${tipo.nombre} a la mascota: ${mascota.nombre}`);
      }
    });
  }*/

  /*asignarNombresRazas() {
    this.mascotas.forEach(mascota => {
      const raza = this.razas.find((r => r.id_raza === mascota.id_raza));
      if (raza) {
        mascota.raza = raza;
        console.log(`Raza asignada: ${raza.nombre} a la mascota: ${mascota.nombre}`);
      }
    });
  }*/

  abrirModal(mascota: Mascota){
    this.mascota = mascota;
    //this.buscarTipo(mascota);

    this.mascotaService.buscarTipoMascota(mascota).subscribe(res => {
      this.mascota.tipo_mascota = res?.nombre;
      this.cdRef.detectChanges();
    });

    this.mascotaService.buscarRaza(mascota).subscribe(res => {
      this.mascota.raza = res?.nombre;
      this.cdRef.detectChanges();
    });

    // Cargar características complementarias
    this.mascota.caracteristicas = [];

    this.mascotaService.listarCarComplementarias().subscribe(listaCaracteristicas => {
      listaCaracteristicas.forEach((car: Caracteristica) => {
        this.mascotaService.buscarCarMascota(mascota, car.id_caracteristica).subscribe(relacion => {
          if (relacion && relacion.valor) {
            this.mascota.caracteristicas.push({ nombre: car.nombre, valor: relacion.valor });
            this.cdRef.detectChanges();
          }
        });
      });
    });

    this.modal.show();
    //this.cdRef.detectChanges();
  }

  cerrarModal(){
    this.mascota = new Mascota(0, 0, 0, '', '', new Date(), '', 0, 0, new Date(), false, false,
      new TipoMascota(0, '', ''),
      new Raza(0, '', ''), '');
    this.modal.hide();
    this.cdRef.detectChanges();
  }

  get mascotasPaginadas(): Mascota[] {
    const start = (this.currentPage - 1) * this.itemsPerPage;
    return this.mascotas.slice(start, start + this.itemsPerPage);
  }

  cambiarPagina(pagina: number) {
    this.currentPage = pagina;
  }
}