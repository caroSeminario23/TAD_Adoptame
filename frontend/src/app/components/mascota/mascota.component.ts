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
    //private mascotaService: MascotaService,
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
    // this.mascotaService.list().subscribe(
    //   data => {
    //     this.mascotas = data;
    //   }
    // );
  }

  listaTipo(){
    // this.mascotaService.typesList().subscribe(
    //   data => {
    //     this.tipos = data;
    //   }
    // );
  }

  listaRaza(){
    // this.mascotaService.breedList().subscribe(
    //   data => {
    //     this.razas = data;
    //   }
    // );
  }

  abrirModal(mascota: Mascota){
    this.mascota = mascota;
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


