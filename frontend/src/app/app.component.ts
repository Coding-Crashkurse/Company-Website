import { Component } from '@angular/core';
import { NavbarComponent } from './navbar/navbar.component';
import { RouterOutlet } from '@angular/router';

@Component({
  standalone: true,
  selector: 'app-root',
  template: `
    <app-navbar></app-navbar>
    <div style="padding: 1rem;">
      <router-outlet></router-outlet>
    </div>
  `,
  imports: [NavbarComponent, RouterOutlet],
})
export class AppComponent {}
