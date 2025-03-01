import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { CoursesComponent } from './courses/courses.component';
import { YoutubeComponent } from './youtube/youtube.component';
import { UdemyComponent } from './udemy/udemy.component';
import { AboutComponent } from './about/about.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'courses', component: CoursesComponent },
  { path: 'youtube', component: YoutubeComponent },
  { path: 'udemy', component: UdemyComponent },
  { path: 'about', component: AboutComponent },
  { path: '**', redirectTo: '' },
];
