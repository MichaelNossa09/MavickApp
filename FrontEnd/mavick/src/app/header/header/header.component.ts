import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Emitters } from 'src/app/emitters/emitters';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  autenticado = false;
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    Emitters.outhEmitter.subscribe((auth: boolean) => {
      this.autenticado = auth;
    })
  }


  logout(): void{
    this.http.post('http://localhost:8000/api/logout', {}, {withCredentials:true}).subscribe(() => {
      this.autenticado = false;
    })
  }

}
