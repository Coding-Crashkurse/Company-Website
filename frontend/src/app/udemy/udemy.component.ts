import { Component, OnInit, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';

@Component({
  standalone: true,
  selector: 'app-udemy',
  templateUrl: './udemy.component.html',
  styleUrls: ['./udemy.component.css'],
  imports: [CommonModule, MatCardModule, MatButtonModule],
})
export class UdemyComponent implements OnInit, OnDestroy {
  courses: any[] = [];
  private intervals: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    // Fetch the courses from your FastAPI backend
    this.http
      .get<any[]>('http://localhost:5555/api/courses')
      .subscribe((res) => {
        this.courses = res;
        // For each course that has an active promo, start a countdown
        this.courses.forEach((course) => {
          if (course.promocode && course.promocode.active) {
            // Initialize the fields to display
            course.days = 0;
            course.hours = 0;
            course.minutes = 0;
            course.seconds = 0;
            this.startCountdown(course);
          }
        });
      });
  }

  startCountdown(course: any) {
    const expiryTime = new Date(course.promocode.expires_at).getTime();
    const intervalId = setInterval(() => {
      const now = Date.now();
      const diff = expiryTime - now;
      if (diff <= 0) {
        course.days = 0;
        course.hours = 0;
        course.minutes = 0;
        course.seconds = 0;
        course.expired = true;
        clearInterval(intervalId);
        return;
      }
      // Calculate days, hours, minutes, seconds
      course.days = Math.floor(diff / (1000 * 60 * 60 * 24));
      course.hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
      course.minutes = Math.floor((diff / (1000 * 60)) % 60);
      course.seconds = Math.floor((diff / 1000) % 60);
    }, 1000);

    this.intervals.push(intervalId);
  }

  ngOnDestroy(): void {
    // Clear all intervals
    this.intervals.forEach((intervalId) => clearInterval(intervalId));
  }
}
