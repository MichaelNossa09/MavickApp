import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {HttpClient} from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class SharedService {

  readonly APIUrl = "http://127.0.0.1:8000";
  readonly PhotoUrl = "http://127.0.0.1:8000/media/";
  constructor(private http: HttpClient) { }

  
  // addClient(val:any){
  //   return this.http.post(this.APIUrl + '/cliente/', val);
  // }

  // updateClient(val: any){
  //   return this.http.put(this.APIUrl + '/cliente/', val);
  // }

  // deleteClient(val: any){
  //   return this.http.delete(this.APIUrl + '/cliente/' + val);
  // }

  // cargarImagen(val:any){
  //   return this.http.post(this.APIUrl + '/SaveFile/', val);
  // }
}
