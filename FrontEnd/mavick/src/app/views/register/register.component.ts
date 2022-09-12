import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  constructor(private http: HttpClient,
    private formBuilder: FormBuilder,
    private router: Router) { }
    email : string;
  form: FormGroup;
  ngOnInit(): void {
    this.form = this.formBuilder.group({
      nombre: '',
      apellido: '',
      email: '',
      password: '',
      telefono: ''
    });
  }


  submit(): void {

    this.http.post('http://localhost:8000/api/register', this.form.getRawValue()).subscribe(()=> {
      this.router.navigate(['/login']);
    });
  }

}
