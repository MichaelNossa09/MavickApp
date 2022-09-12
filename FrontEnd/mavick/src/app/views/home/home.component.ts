import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Emitters } from 'src/app/emitters/emitters';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  user = {
    id: 0,
    email: '',
    password: '',
    nombre: '',
    apellido: '',
    telefono: ''
  }
  constructor(private http: HttpClient) { }

  ngOnInit(): void {

    this.http.get('http://localhost:8000/api/user', {withCredentials:true}).subscribe((res:any)=> {

      this.user.id = res.id;
      this.user.email = res.email;
      this.user.nombre = res.nombre;
      this.user.apellido = res.apellido;
      this.user.telefono = res.telefono;

      Emitters.outhEmitter.emit(true);
    },
      err => {
        Emitters.outhEmitter.emit(false);
      });
  }



}
