import geopandas as gpd
from shapely.geometry import Polygon, MultiPolygon
import numpy as np
from scipy.spatial import cKDTree

# Define tolerance for snapping (in degrees or meters depending on CRS)
SNAP_TOLERANCE = 0.00015  # Adjust tolerance based on your needs

def snap_polygons_with_clustering(gdf, tolerance=SNAP_TOLERANCE):
    # Step 1: Extract all vertices
    vertices = []
    poly_indices = []
    for idx, geom in enumerate(gdf.geometry):
        if geom.is_valid:
            # Extract each point in the polygon/multipolygon
            if geom.geom_type == 'Polygon':
                coords = list(geom.exterior.coords)
                vertices.extend(coords)
                poly_indices.extend([idx] * len(coords))
            elif geom.geom_type == 'MultiPolygon':
                for poly in geom:
                    coords = list(poly.exterior.coords)
                    vertices.extend(coords)
                    poly_indices.extend([idx] * len(coords))

    # Step 2: Use cKDTree to find clusters of close vertices
    vertices = np.array(vertices)
    tree = cKDTree(vertices)
    clusters = tree.query_ball_tree(tree, tolerance)

    # Step 3: Deduplicate clusters (remove overlapping groups)
    unique_clusters = []
    seen = set()
    for cluster in clusters:
        unique_cluster = tuple(sorted(set(cluster)))
        if unique_cluster not in seen:
            seen.add(unique_cluster)
            unique_clusters.append(unique_cluster)

    # Step 4: Snap vertices in each cluster to the cluster centroid
    snapped_vertices = vertices.copy()
    for cluster in unique_clusters:
        # Calculate the centroid of the cluster
        cluster_points = vertices[list(cluster)]
        centroid = cluster_points.mean(axis=0)
        for index in cluster:
            snapped_vertices[index] = centroid

    # Step 5: Reconstruct polygons with snapped vertices
    new_geometries = []
    vertex_idx = 0
    for idx, geom in enumerate(gdf.geometry):
        if geom.is_valid:
            if geom.geom_type == 'Polygon':
                coords = snapped_vertices[vertex_idx:vertex_idx + len(geom.exterior.coords)]
                new_geom = Polygon(coords)
                vertex_idx += len(geom.exterior.coords)
            elif geom.geom_type == 'MultiPolygon':
                polygons = []
                for poly in geom:
                    coords = snapped_vertices[vertex_idx:vertex_idx + len(poly.exterior.coords)]
                    polygons.append(Polygon(coords))
                    vertex_idx += len(poly.exterior.coords)
                new_geom = MultiPolygon(polygons)
            new_geometries.append(new_geom)
        else:
            new_geometries.append(geom)

    gdf.geometry = new_geometries
    return gdf

# Load the GeoJSON file
gdf = gpd.read_file("sanborn_sanFrancisco_vol10_1940.geojson")

# Snap polygon vertices with clustering
snapped_gdf = snap_polygons_with_clustering(gdf)

# Save to a new GeoJSON file
snapped_gdf.to_file("snapped_output2.geojson", driver="GeoJSON")
