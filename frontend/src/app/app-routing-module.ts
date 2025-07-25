import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {MascotaComponent} from './components/mascota/mascota.component';
import {HomeComponent} from './components/home/home.component';
import {AboutComponent} from './components/about/about.component';

const routes: Routes = [
  { path: 'catalogo', component: MascotaComponent },
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
