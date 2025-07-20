import {ChangeDetectorRef, Component, OnInit} from '@angular/core';
import {Mascota} from '../../models/mascota';
import {TipoMascota} from '../../models/tipo-mascota';
import {Raza} from '../../models/raza';
import {MascotaService} from '../../services/mascota/mascota.service';

declare var window: any;

@Component({
  selector: 'app-mascota',
  standalone: false,
  templateUrl: './mascota.component.html',
  styleUrl: './mascota.component.css'
})
export class MascotaComponent implements OnInit {
  mascota: Mascota = new Mascota(0, 0, 0, '', '', new Date(), '', 0, 0, new Date(), false, false,
    new TipoMascota(0, ''),
    new Raza(0, ''));
  mascotas: Mascota[] = [];
  tipos: TipoMascota[] = [];
  razas: Raza[] = [];
  modal: any;

  constructor(
    private mascotaService: MascotaService,
    private cdRef: ChangeDetectorRef
  ) {
  }

  ngOnInit(): void {
    this.modal = new window.bootstrap.Modal(document.getElementById('Modal'));
    this.lista();
    this.listaTipo();
    this.listaRaza();
  }

  lista(){
    this.mascotaService.list().subscribe(
      data => {
        this.mascotas = data;
        this.asignarNombresTipos(); 
        this.asignarNombresRazas(); 
      },
      error => console.error("Error al obtener la lista de mascotas:", error)
    );
      
  }

  listaTipo(){
    this.mascotaService.listarTipos().subscribe(
      data => {
        this.tipos = data;
        this.asignarNombresTipos();
      }
    );
  }

  listaRaza(){
    this.mascotaService.listarRazas().subscribe(
      data => {
        this.razas = data;
        this.asignarNombresRazas();
      }
    );
  }
    

  buscarTipo(mascota: any) {
    this.mascotaService.buscarTipo(mascota).subscribe(
      data => {
        mascota.tipo_mascota = data.nombre;
      },
      error => {
        console.error("Error al buscar tipo de mascota:", error);
      }
    );
  }

  asignarNombresTipos() {
    this.mascotas.forEach(mascota => {
      const tipo = this.tipos.find((t => t.id_tipo_mascota === mascota.id_tipo_mascota));
      if (tipo) {
        mascota.tipo_mascota = tipo;
        console.log(`Tipo asignado: ${tipo.nombre} a la mascota: ${mascota.nombre}`);
      }
    });
  }

  asignarNombresRazas() {
    this.mascotas.forEach(mascota => {
      const raza = this.razas.find((r => r.id_raza === mascota.id_raza));
      if (raza) {
        mascota.raza = raza;
        console.log(`Raza asignada: ${raza.nombre} a la mascota: ${mascota.nombre}`);
      }
    });
  }


  abrirModal(mascota: Mascota){
    this.mascota = mascota;
    //this.buscarTipo(mascota);
    this.modal.show();
    this.cdRef.detectChanges();
  }

  cerrarModal(){
    this.mascota = new Mascota(0, 0, 0, '', '', new Date(), '', 0, 0, new Date(), false, false,
      new TipoMascota(0, ''),
      new Raza(0, ''));
    this.modal.hide();
    this.cdRef.detectChanges();
  }
}


